from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routers.v1.items import item_router


# Initialize db
Base.metadata.create_all(bind=engine) 

# Create app
app = FastAPI()

# include routers
app.include_router(item_router)