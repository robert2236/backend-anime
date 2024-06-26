from typing import Optional
from pydantic import BaseModel, Field, validator
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values, **kwargs):
     if not ObjectId.is_valid(v):
        raise ValueError('Invalid ObjectId')
     return str(v)
    

class Anime(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    name: str
    img: str
    category: str
    sub: bool
    dub: bool
    file: str

class UpdateAnime(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    name: Optional[str] = None
    img: Optional[str] = None
    common_name: Optional[str] = None
    category: Optional[str] = None
    sub: Optional[bool] = None
    dub: Optional[str] = None
    file: Optional[str] = None


class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }