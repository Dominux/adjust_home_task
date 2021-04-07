from typing import Optional, List, Tuple, Dict
from datetime import date

from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/", response_model=List[schemas.Metrics])
def read_metrics(
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    filter_by: Optional[List[str]] = Query(None),
    group_by: Optional[List[str]] = Query(None),
    order_by: Optional[str] = None,
    db: Session = Depends(get_db)
    ):
    """
        :param date_from date
        :param date_to   date
        :param filters   list - ["country: US, RU, ...", ...]
        :param group_by  list - ["country", "os", "date", ...]
        :param order_by      str  - "clicks.asc"

    """

    # Preparing arguments for crud
    filters = _get_filters(filter_by)
    order_by = order_by.split(".") if order_by else None

    return crud.get_metrics(
        db=db,
        date_from=date_from,
        date_to=date_to,
        filters=filters,
        group_by=group_by,
        order_by=order_by,
    )


def _get_filters(filters: Optional[List[str]]) -> dict:
    result = {}

    if filters:
        for _filter in filters:
            col, val = _filter.replace(" ", "").split(":")
            result[col] = val.split(",")

    return result

