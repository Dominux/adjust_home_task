from datetime import date
from typing import Optional, List, Tuple, Dict

from sqlalchemy import asc, desc, func
from sqlalchemy.orm import Session

from . import models, schemas


def get_metrics(
    db: Session,
    filters: Dict[str, List[str]],
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    group_by: Optional[List[str]] = None,
    order_by: Optional[Tuple[str, str]] = None,
    ) -> list:

    # Getting filters
    filters = [
        func.lower(
            getattr(models.Metrics, k)
        ).in_(
            map(func.lower, v)
        ) for k, v in filters.items()
    ]
    if date_from:
        filters.append(models.Metrics.date >= date_from)
    if date_to:
        filters.append(models.Metrics.date <= date_to)

    # Getting group_by
    group_by = [getattr(models.Metrics, col) for col in group_by] if group_by else []

    # Getting order_by
    if order_by:
        _func = asc if order_by[1] == 'asc' else desc
        order_by = _func(getattr(models.Metrics, order_by[0]))

    return db.query(models.Metrics)\
            .filter(*filters)\
            .group_by(*group_by)\
            .order_by(order_by)\
            .all()

