from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logger
from app.db.database import Base, engine
from app.api.routes.inventry_routes import router as student_router

# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}