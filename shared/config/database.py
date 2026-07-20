from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from shared.config.environment import env

DATABASE_URL = (
    f"mysql+pymysql://{env.DB_USERNAME}:{env.DB_PASSWORD}"
    f"@{env.DB_HOST}:{env.DB_PORT}/{env.DB_DATABASE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    echo=env.DEBUG,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
