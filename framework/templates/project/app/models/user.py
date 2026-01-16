from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
  id: int
  created_at: datetime = datetime.now().isoformat()