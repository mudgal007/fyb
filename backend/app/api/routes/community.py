from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.community import CommunityEvent, CommunityPost
from app.models.user import User
from app.schemas.community import (
    CommunityEventCreate,
    CommunityEventRead,
    CommunityEventUpdate,
    CommunityPostCreate,
    CommunityPostRead,
    CommunityPostUpdate,
)
from app.services.personalization import daily_welcome_message
from app.utils import deps

router = APIRouter()


@router.get("/welcome")
async def welcome_message(current_user: Annotated[User, Depends(deps.get_current_active_user)]):
    return {"message": daily_welcome_message(current_user.full_name)}


@router.get("/posts", response_model=list[CommunityPostRead])
async def list_posts(session: Annotated[AsyncSession, Depends(get_session)]):
    result = await session.execute(select(CommunityPost))
    return list(result.scalars().all())


@router.post("/posts", response_model=CommunityPostRead, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_in: CommunityPostCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    post = CommunityPost(**post_in.model_dump(), owner_id=current_user.id)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


@router.put("/posts/{post_id}", response_model=CommunityPostRead)
async def update_post(
    post_id: int,
    post_in: CommunityPostUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(CommunityPost).where(CommunityPost.id == post_id, CommunityPost.owner_id == current_user.id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    for key, value in post_in.model_dump(exclude_unset=True).items():
        setattr(post, key, value)
    await session.commit()
    await session.refresh(post)
    return post


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(CommunityPost).where(CommunityPost.id == post_id, CommunityPost.owner_id == current_user.id))
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    await session.delete(post)
    await session.commit()
    return None


@router.get("/events", response_model=list[CommunityEventRead])
async def list_events(session: Annotated[AsyncSession, Depends(get_session)]):
    result = await session.execute(select(CommunityEvent))
    return list(result.scalars().all())


@router.post("/events", response_model=CommunityEventRead, status_code=status.HTTP_201_CREATED)
async def create_event(
    event_in: CommunityEventCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    event = CommunityEvent(**event_in.model_dump(), creator_id=current_user.id)
    session.add(event)
    await session.commit()
    await session.refresh(event)
    return event


@router.put("/events/{event_id}", response_model=CommunityEventRead)
async def update_event(
    event_id: int,
    event_in: CommunityEventUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(CommunityEvent).where(CommunityEvent.id == event_id, CommunityEvent.creator_id == current_user.id))
    event = result.scalar_one_or_none()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    for key, value in event_in.model_dump(exclude_unset=True).items():
        setattr(event, key, value)
    await session.commit()
    await session.refresh(event)
    return event


@router.delete("/events/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(
    event_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
):
    result = await session.execute(select(CommunityEvent).where(CommunityEvent.id == event_id, CommunityEvent.creator_id == current_user.id))
    event = result.scalar_one_or_none()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    await session.delete(event)
    await session.commit()
    return None
