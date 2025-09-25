from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.database import get_session
from app.models.user import User, UserRole
from app.schemas.user import UserCreate, UserRead
from app.utils import deps
from app.utils.security import create_access_token, get_password_hash, verify_password

router = APIRouter()
settings = get_settings()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate, session: Annotated[AsyncSession, Depends(get_session)]):
    existing_user = await session.execute(select(User).where(User.email == user_in.email))
    if existing_user.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
        role=user_in.role,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.post("/token")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    result = await session.execute(select(User).where(User.email == form_data.username))
    user = result.scalar_one_or_none()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(user.email, timedelta(minutes=settings.access_token_expire_minutes))
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserRead)
async def read_current_user(current_user: Annotated[User, Depends(deps.get_current_active_user)]):
    return current_user


@router.get("/admin/dashboard", response_model=list[UserRead])
async def admin_list_users(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(deps.get_current_admin_user)],
):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return list(users)
