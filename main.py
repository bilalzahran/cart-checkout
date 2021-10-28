from fastapi import FastAPI, Request
from starlette.responses import Response as res

from src.dependency.dependency import container
from src.handler.api_handler.v1 import api_router
from src.utils.log_helper import LogHelper

app = FastAPI(docs_url="/docs")


@app.on_event("startup")
async def startup():
    print("startup connect")
    await container.database().connect()


@app.on_event("shutdown")
async def shutdown():
    print("startup shutdown")
    await container.database().disconnect()


@app.exception_handler
async def server_failure_exception_handler(request: Request, failure):
    LogHelper.log_error(failure)

    return res(media_type="application/json", status_code=500)


app.include_router(api_router)
