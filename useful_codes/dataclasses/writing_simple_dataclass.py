from dataclasses import dataclass, field
from typing import List

@dataclass
class Ticket:
    id: str
    name: str
    text: str
    times_visited: int
    # when adding an object to a dataclass with defaukt values as list or tuples or dict
    # do not simply list them as u would for str or int
    # defaults as List[] or list[str] would fail, 
    # they need to give the List[str] a default field value
    sections_visited: List[str] = field(default_factory = List)


#reviews = [
#     {"id": "R001", "text": "Great music, but the queue was awful"},
#     {"id": "R002", "text": "The food was excellent"},
# ]
