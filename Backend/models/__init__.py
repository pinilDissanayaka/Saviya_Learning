from database.database import Base, engine

Base.metadata.create_all(engine)
