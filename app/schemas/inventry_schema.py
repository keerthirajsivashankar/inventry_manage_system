from pydantic import BaseModel, ConfigDict , Field
from typing import Optional

class ItemCreate(BaseModel):
    name: str = Field(...,min_length=1,max_length=100)
    price : int = Field(..., gt=0)
    qty : int = Field(..., ge=0)
    description : Optional[str] = Field(None, max_length=255)
    
class ItemResponse(BaseModel):

    id: int
    name: str
    price : int
    qty : int
    description : str

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    price: Optional[int] = Field(None, gt=0)
    qty: Optional[int] = Field(None, ge=0)
    description: Optional[str] = Field(None, max_length=255)

    model_config = ConfigDict(from_attributes=True)

