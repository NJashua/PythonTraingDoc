from sqlalchemy import create_engine

class Settings:
    database_url = "sqlite:///./test.db"  # or your actual SQLite database file path

settings = Settings()

# SQLite Database URL
SQLALCHEMY_DATABASE_URL = settings.database_url

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Example of how to use the engine to connect and check the connection
try:
    with engine.connect() as connection:
        print("Database connection successful.")
except Exception as e:
    print(f"Database connection failed: {e}")
