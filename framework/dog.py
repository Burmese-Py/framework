from pydantic import BaseModel
from datetime import datetime

class Dog(BaseModel):
  id: int
  created_at: datetime