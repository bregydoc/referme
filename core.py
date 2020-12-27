from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel


class ProcessInput(BaseModel):
    urls: List[str]


@dataclass
class Publication:
    title: str
    author: List[str]
    year: str
    references: int
