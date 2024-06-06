from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MagneticFieldMap():
    __tablename__ = 'magnetic_field_map'
    id = Column(Integer, primary_key=True, autoincrement=True)
    coordinate_x = Column(String, nullable=False)
    coordinate_y = Column(String, nullable=False)
    magnetic_field_x = Column(String, nullable=False)
    magnetic_field_y = Column(String, nullable=False)
    magnetic_field_z = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=current_timestamp())
