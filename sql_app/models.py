from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Enum
from sqlalchemy.ext.hybrid import hybrid_property

from .database import Base


class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    channel = Column(String)
    country = Column(String)
    os = Column(String)
    impressions = Column(Integer)
    clicks = Column(Integer)
    installs = Column(Integer)
    spend = Column(Float)
    revenue = Column(Float)

    @hybrid_property
    def cpi(self):
        try:
            return self.spend / self.installs
        except ZeroDevisionError:
            return None

