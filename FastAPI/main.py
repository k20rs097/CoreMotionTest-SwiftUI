from fastapi import FastAPI
from pydantic import BaseModel

import db_model
import db_setting

class MagneticFieldMapBase(BaseModel):
    coordinate_x: str
    coordinate_y: str
    magnetic_field_x: str
    magnetic_field_y: str
    magnetic_field_z: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/fields", tags=["fields"])
def read_fields():
    result = s.session.query(db_model.MagneticFieldMap).all()
    return result

@app.post("/fields", tags=["fields"])
def create_field(data: MagneticFieldMapBase):
    field = db_model.MagneticFieldMap()
    session = db_setting.session()
    db_setting.session.add(field)
    try:
        field.coordinate_x = data.coordinate_x
        field.coordinate_y = data.coordinate_y
        field.magnetic_field_x = data.magnetic_field_x
        field.magnetic_field_y = data.magnetic_field_y
        field.magnetic_field_z = data.magnetic_field_z
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

@app.put("/fields/{id}", tags=["fields"])
def update_field(id: int, data:UserBase):
    session = db_setting.session()
    try:
        db_setting.session.query(db_model.MagneticFieldMap).\
        filter(db_model.MagneticFieldMap.id == id).\
        update({
            "coordinate_x": data.coordinate_x,
            "coordinate_y": data.coordinate_y,
            "magnetic_field_x": data.magnetic_field_x,
            "magnetic_field_x": data.magnetic_field_y,
            "magnetic_field_x": data.magnetic_field_z    
        })
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()