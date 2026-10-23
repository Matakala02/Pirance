import re

from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import DuplicateUserError, InvalidCredentialsError
from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, data: UserCreate) -> User:
    existing = db.scalar(
        select(User).where(or_(User.email == data.email, User.phone == data.phone))
    )
    if existing:
        raise DuplicateUserError()

    user = User(
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise DuplicateUserError()
    db.refresh(user)
    return user


def authenticate(db: Session, identifier: str, password: str) -> User:
    identifier = identifier.strip()
    if "@" in identifier:
        identifier = identifier.lower()
    else:
        identifier = re.sub(r"[\s-]", "", identifier)

    user = db.scalar(
        select(User).where(or_(User.email == identifier, User.phone == identifier))
    )
    if user is None or not verify_password(password, user.password_hash):
        raise InvalidCredentialsError()
    return user