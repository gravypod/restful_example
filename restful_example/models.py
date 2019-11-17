from dataclasses import dataclass
from typing import Optional


class Thing:
    id: Optional[str]
    name: str
    size: int

    def __init__(self, thing_id: Optional[str], name: str, size: int):
        self.id = thing_id
        self.name = name
        self.size = size

    def __eq__(self, other):
        if isinstance(other, Thing):
            return other.id == self.id

        return False

    def to_dict(self) -> dict:
        data = {
            'name': self.name,
            'size': self.size
        }

        if self.id is not None:
            data['id'] = self.id

        return data

    @staticmethod
    def from_dict(data: dict) -> 'Thing':

        if 'id' in data and data['id'] is not None:
            thing_id = data['id']
        else:
            thing_id = None

        return Thing(
            thing_id=thing_id,
            name=str(data['name']),
            size=int(data['size']),
        )
