from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.personal import PersonalItem
from app.models.user import User
from app.schemas.personal import PersonalItemCreate, PersonalItemRead, PersonalItemUpdate
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[PersonalItemRead])
async def list_personal_items(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(PersonalItem).where(PersonalItem.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=PersonalItemRead, status_code=status.HTTP_201_CREATED)
async def create_personal_item(
    personal_in: PersonalItemCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    item = PersonalItem(**personal_in.model_dump(), owner_id=current_user.id)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


@router.put("/{item_id}", response_model=PersonalItemRead)
async def update_personal_item(
    item_id: int,
    personal_in: PersonalItemUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(PersonalItem).where(PersonalItem.id == item_id, PersonalItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personal item not found")

    for key, value in personal_in.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    await session.commit()
    await session.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personal_item(
    item_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(PersonalItem).where(PersonalItem.id == item_id, PersonalItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personal item not found")

    await session.delete(item)
    await session.commit()
    return None
