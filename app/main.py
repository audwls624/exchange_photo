from dataclasses import asdict

import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from fastapi.security import APIKeyHeader
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.common.config import conf
from app.databases.connections import db
from app.middlewares.trusted_hosts import TrustedHostMiddleware
from app.routes import index

API_KEY_HEADER = APIKeyHeader(name="Authorization", auto_error=False)

c = conf()
conf_dict = asdict(c)
app = FastAPI()
db.init_app(app, **conf_dict)

# 미들웨어 정의(밑에 정의된 middleware 부터 실행 시작)
app.add_middleware(
    CORSMiddleware,
    allow_origins=conf().ALLOW_SITE,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=conf().TRUSTED_HOSTS, except_path=["/health"])

# router 정의
app.include_router(index.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

