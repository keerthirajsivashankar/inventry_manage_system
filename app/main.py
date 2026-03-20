from fastapi import FastAPI, Request
from app.core.config import settings
from app.core.logger import setup_logger
from app.db.database import Base, engine
from app.api.routes.inventry_routes import router as student_router
from app.utils.exceptions import ItemNotFoundException
from app.utils.responses import error_response
from fastapi.responses import JSONResponse

# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(student_router)

@app.exception_handler(ItemNotFoundException)
async def not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=404,
        content=error_response(message=exc.detail, code=404)
    )


@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}