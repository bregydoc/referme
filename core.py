from typing import List, Optional
from pydantic import BaseModel


class ProcessInput(BaseModel):
    urls: List[str]
