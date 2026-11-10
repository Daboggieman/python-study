from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Ticket:
    id: str
    name: str
    text: str
    times_visited: int
    # when adding an object to a dataclass with defaukt values as list or tuples or dict
    # do not simply list them as u would for str or int
    # defaults as List[] or list[str] would fail, 
    # they need to give the List[str] a default field value as default_factory = List
    # The same applies to dicts (default_factory=dict)
    sections_visited: List[str] = field(default_factory = List)
    payments: Dict = field(default_factory = Dict)


# example 2:

@dataclass
class Team:
    id: str
    team_name: str
    coach: str
    strenghts: List[str] = field(default_factory=List)
    total_players: int = 11
    goals: int = 0

team_a = Team("T001", "first team", "short ahh nigga", ["passing", "control", "defence", "speed", "tactics"])
team_b = Team("T002", "second team", "tall ahh nigga")


team_a.strenghts.append("durability")
team_a.strenghts.append("hax")

