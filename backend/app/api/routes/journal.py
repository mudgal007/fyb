from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.journal import JournalEntry
from app.models.user import User
from app.schemas.journal import JournalCreate, JournalRead, JournalUpdate
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=list[JournalRead])
async def list_journal_entries(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(JournalEntry).where(JournalEntry.owner_id == current_user.id))
    return list(result.scalars().all())


@router.post("/", response_model=JournalRead, status_code=status.HTTP_201_CREATED)
async def create_journal_entry(
    journal_in: JournalCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    journal = JournalEntry(**journal_in.model_dump(), owner_id=current_user.id)
    session.add(journal)
    await session.commit()
    await session.refresh(journal)
    return journal


@router.put("/{entry_id}", response_model=JournalRead)
async def update_journal_entry(
    entry_id: int,
    journal_in: JournalUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(
        select(JournalEntry).where(JournalEntry.id == entry_id, JournalEntry.owner_id == current_user.id)
    )
    journal = result.scalar_one_or_none()
    if not journal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found")

    for key, value in journal_in.model_dump(exclude_unset=True).items():
        setattr(journal, key, value)
    await session.commit()
    await session.refresh(journal)
    return journal


@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_entry(
    entry_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(
        select(JournalEntry).where(JournalEntry.id == entry_id, JournalEntry.owner_id == current_user.id)
    )
    journal = result.scalar_one_or_none()
    if not journal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found")

    await session.delete(journal)
    await session.commit()
    return None
