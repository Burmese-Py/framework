from pydantic import BaseModel
from datetime import datetime

class Model(BaseModel):
  id: int
  created_at: datetime