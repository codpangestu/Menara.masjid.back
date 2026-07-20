from sqlalchemy.orm import Session
from shared.models.users import Users


def get_user_by_email(db: Session, email: str) -> Users | None:
    return db.query(Users).filter(Users.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> Users | None:
    return db.query(Users).filter(Users.id_user == user_id).first()


def create_user(db: Session, **kwargs) -> Users:
    user = Users(**kwargs)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_last_login(db: Session, user: Users) -> None:
    from datetime import datetime
    user.last_login = datetime.utcnow()
    db.commit()
