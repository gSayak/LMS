# database.py
import databases
import sqlalchemy
DATABASE_URL = ""

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)