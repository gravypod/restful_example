from random import sample

from werkzeug.exceptions import NotFound, BadRequest

from restful_example.models import Thing
from string import ascii_letters, digits


class ThingRegistry:
    def __init__(self):
        self.things = []

    def list(self):
        return self.things

    def create(self, thing: Thing) -> Thing:
        if thing.id is not None:
            raise BadRequest('Cannot create a thing and provide an ID!')

        created = Thing(
            thing_id=''.join(sample((ascii_letters + digits) * 2, k=10)),
            name=thing.name,
            size=thing.size
        )
        self.things.append(created)
        return created

    def get(self, thing_id: str):
        for thing in self.things:
            if thing.id == thing_id:
                return thing
        else:
            raise NotFound(f'Thing with ID {thing_id} was not found')

    def delete(self, thing: Thing):
        if thing not in self.things:
            raise NotFound(f'Thing was not found.')

        self.things.remove(thing)

    def update(self, updates: dict, thing: Thing) -> Thing:
        if 'id' in updates and thing.id != updates['id']:
            raise BadRequest('Cannot change an ID!')

        created = Thing.from_dict({
            **thing.to_dict(),
            **updates
        })
        self.things.remove(thing)
        self.things.append(created)
        return created
