from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.planner import PlannerItem
from app.models.user import User
from app.schemas.planner import PlannerItemCreate, PlannerItemRead, PlannerItemUpdate
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[PlannerItemRead])
async def list_planner_items(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(PlannerItem).where(PlannerItem.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=PlannerItemRead, status_code=status.HTTP_201_CREATED)
async def create_planner_item(
    planner_in: PlannerItemCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    item = PlannerItem(**planner_in.model_dump(), owner_id=current_user.id)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


@router.put("/{item_id}", response_model=PlannerItemRead)
async def update_planner_item(
    item_id: int,
    planner_in: PlannerItemUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(PlannerItem).where(PlannerItem.id == item_id, PlannerItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Planner item not found")

    for key, value in planner_in.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    await session.commit()
    await session.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_planner_item(
    item_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(PlannerItem).where(PlannerItem.id == item_id, PlannerItem.owner_id == current_user.id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Planner item not found")

    await session.delete(item)
    await session.commit()
    return None
