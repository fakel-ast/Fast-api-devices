import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from core.config import settings
from core.apps.routes import api_router
from core.config.settings import PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
    description="Author - Fakel_ast",
    version="0.1.0",
)


app.include_router(api_router, prefix=settings.API_V1_STR)


register_tortoise(
    app,
    db_url=settings.DATABASE_URI,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, debug=True, reload=True)
