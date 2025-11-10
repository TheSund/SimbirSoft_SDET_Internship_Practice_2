from typing import List

from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int


class EntityCreate(BaseModel):
    title: str
    verified: bool
    important_numbers: List[int]
    addition: Addition

    def build(self) -> dict:
        return self.model_dump()

class Entity(EntityCreate):
    id: int