from pydantic import BaseModel
from datetime import date


class Metrics(BaseModel):
    date: date
    channel: str
    country: str
    os: str
    impressions: int
    clicks: int
    installs: int
    spend: float
    revenue: float
    cpi: float

    class Config:
        orm_mode = True

