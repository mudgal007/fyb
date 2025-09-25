from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.tracker import TrackerItem
from app.models.user import User
from app.schemas.tracker import TrackerItemCreate, TrackerItemRead, TrackerItemUpdate
from app.services.personalization import nudge_for_goal_progress
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[TrackerItemRead])
async def list_tracker_items(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(TrackerItem).where(TrackerItem.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=TrackerItemRead, status_code=status.HTTP_201_CREATED)
async def create_tracker_item(
    tracker_in: TrackerItemCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    item = TrackerItem(**tracker_in.model_dump(), owner_id=current_user.id)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


@router.put("/{item_id}", response_model=TrackerItemRead)
async def update_tracker_item(
    item_id: int,
    tracker_in: TrackerItemUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(TrackerItem).where(TrackerItem.id == item_id, TrackerItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tracker item not found")

    for key, value in tracker_in.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    await session.commit()
    await session.refresh(item)
    return item


@router.get("/{item_id}/nudge")
async def tracker_goal_nudge(
    item_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(TrackerItem).where(TrackerItem.id == item_id, TrackerItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tracker item not found")
    progress = 1.0 if item.is_complete else 0.5
    return {"message": nudge_for_goal_progress(item.title, progress)}


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tracker_item(
    item_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(TrackerItem).where(TrackerItem.id == item_id, TrackerItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tracker item not found")

    await session.delete(item)
    await session.commit()
    return None
