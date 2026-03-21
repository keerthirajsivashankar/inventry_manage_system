from fastapi import FastAPI, Request
from app.core.config import settings
from app.core.logger import setup_logger
from app.db.database import Base, engine
from app.api.routes.inventry_routes import router as item_router
from app.utils.exceptions import ItemNotFoundException
from app.utils.responses import error_response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware



# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(item_router)

@app.exception_handler(ItemNotFoundException)
async def not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=404,
        content=error_response(message=exc.detail, code=404)
    )


@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}