from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.mood import MoodEntry
from app.models.user import User
from app.schemas.mood import MoodCreate, MoodRead, MoodUpdate
from app.services.personalization import generate_mood_suggestion
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[MoodRead])
async def list_moods(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(MoodEntry).where(MoodEntry.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=MoodRead, status_code=status.HTTP_201_CREATED)
async def create_mood(
    mood_in: MoodCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    data = mood_in.model_dump()
    if not data.get("suggestion"):
        data["suggestion"] = generate_mood_suggestion(data["mood"], data.get("intensity", 0.5))
    mood = MoodEntry(**data, owner_id=current_user.id)
    session.add(mood)
    await session.commit()
    await session.refresh(mood)
    return mood


@router.put("/{mood_id}", response_model=MoodRead)
async def update_mood(
    mood_id: int,
    mood_in: MoodUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(MoodEntry).where(MoodEntry.id == mood_id, MoodEntry.owner_id == current_user.id))
    mood = result.scalar_one_or_none()
    if not mood:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mood entry not found")

    for key, value in mood_in.model_dump(exclude_unset=True).items():
        setattr(mood, key, value)
    await session.commit()
    await session.refresh(mood)
    return mood


@router.delete("/{mood_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mood(
    mood_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(MoodEntry).where(MoodEntry.id == mood_id, MoodEntry.owner_id == current_user.id))
    mood = result.scalar_one_or_none()
    if not mood:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mood entry not found")

    await session.delete(mood)
    await session.commit()
    return None
