from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.goal import Goal
from app.models.user import User
from app.schemas.goal import GoalCreate, GoalRead, GoalUpdate
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[GoalRead])
async def list_goals(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Goal).where(Goal.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=GoalRead, status_code=status.HTTP_201_CREATED)
async def create_goal(
    goal_in: GoalCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    goal = Goal(**goal_in.model_dump(), owner_id=current_user.id)
    session.add(goal)
    await session.commit()
    await session.refresh(goal)
    return goal


@router.put("/{goal_id}", response_model=GoalRead)
async def update_goal(
    goal_id: int,
    goal_in: GoalUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Goal).where(Goal.id == goal_id, Goal.owner_id == current_user.id))
    goal = result.scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")

    for key, value in goal_in.model_dump(exclude_unset=True).items():
        setattr(goal, key, value)
    await session.commit()
    await session.refresh(goal)
    return goal


@router.delete("/{goal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_goal(
    goal_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Goal).where(Goal.id == goal_id, Goal.owner_id == current_user.id))
    goal = result.scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")

    await session.delete(goal)
    await session.commit()
    return None
