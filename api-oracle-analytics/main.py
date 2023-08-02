from fastapi import FastAPI
from routers.etl_router import etl_router
from routers.auth_router import auth_router
import uvicorn
import os

app = FastAPI()
app.title = "App ETL Oracle - MySQL"
app.version = "1.0.0"
app.description = "ETL"
app.docs_url = "/docs"
app.include_router(etl_router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)),
                reload=True)