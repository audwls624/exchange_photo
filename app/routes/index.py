from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.requests import Request
from fastapi import Depends
from app.databases.connections import db

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session)):
    """
    ELB 상태 체크용 API
    :param session:
    :return:
    """
    current_time = datetime.utcnow()
    return Response(f"TEST API (UTC: {current_time.strftime('%Y-%m-%dT%H:%M:%S')})")

