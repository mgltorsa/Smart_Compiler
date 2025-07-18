from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncIterator
from shared.logging import get_logger
from server.infrastructure.injections import get_scheduler
from server.infrastructure.controllers.rest.tasks.api import router as tasks_router
from server.infrastructure.controllers.rest.files.api import router as files_router

logger = get_logger()

scheduler = get_scheduler()


@asynccontextmanager
async def app_lifespan(app: FastAPI) -> AsyncIterator[None]:

    scheduler.start()
    logger.info("SmartCompiler REST API started")
    yield
    logger.info("SmartCompiler REST API stopped")
    scheduler.shutdown(wait=False)




    

app = FastAPI(title="SmartCompiler", description="REST API for SmartCompiler", version="0.1.0", lifespan=app_lifespan)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(tasks_router)
app.include_router(files_router)
