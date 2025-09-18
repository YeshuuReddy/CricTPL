import logging
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from app.db.database import init_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
_logger = logging.getLogger("Cric_TPL")

@asynccontextmanager
async def lifespan(_app: FastAPI):
    _logger.info("🚀 Starting Cric_TPL API...")
    init_db()
    _logger.info("✅ Database Initialized")
    yield
    _logger.info("🛑 Shutting down Cric_TPL API...")
app=FastAPI(
    title="Cric_TPL",
    description="Thirumalapuram Premier League",
    version="1.0.0",
    docs_url="/",
    lifespan=lifespan,
    openapi_url="/openapi.json",
    contact={
        "name": "Yaswanth Reddy",
        "email": "yaswanthreddy7474@gmail.com",
    },
    openapi_version="2.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "docExpansion": "none"
        }
    )
@app.get("/welcome", tags=["Root"])
def root():
    return {"message": "Welcome to Cric!, FastAPI + PostgresSQL + SQLModel is ready for use!",
            "docs":"/"
            }

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)





