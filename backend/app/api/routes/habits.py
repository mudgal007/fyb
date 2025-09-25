from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.habit import Habit
from app.models.user import User
from app.schemas.habit import HabitCreate, HabitRead, HabitUpdate
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[HabitRead])
async def list_habits(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Habit).where(Habit.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=HabitRead, status_code=status.HTTP_201_CREATED)
async def create_habit(
    habit_in: HabitCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    habit = Habit(**habit_in.model_dump(), owner_id=current_user.id)
    session.add(habit)
    await session.commit()
    await session.refresh(habit)
    return habit


@router.put("/{habit_id}", response_model=HabitRead)
async def update_habit(
    habit_id: int,
    habit_in: HabitUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Habit).where(Habit.id == habit_id, Habit.owner_id == current_user.id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habit not found")

    for key, value in habit_in.model_dump(exclude_unset=True).items():
        setattr(habit, key, value)
    await session.commit()
    await session.refresh(habit)
    return habit


@router.post("/{habit_id}/increment", response_model=HabitRead)
async def increment_habit(
    habit_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Habit).where(Habit.id == habit_id, Habit.owner_id == current_user.id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habit not found")

    habit.streak += 1
    await session.commit()
    await session.refresh(habit)
    return habit


@router.delete("/{habit_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_habit(
    habit_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(Habit).where(Habit.id == habit_id, Habit.owner_id == current_user.id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habit not found")

    await session.delete(habit)
    await session.commit()
    return None
