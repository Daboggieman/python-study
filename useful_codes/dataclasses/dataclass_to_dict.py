from dataclasses import dataclass, field, asdict

@dataclass
class Person:
    name: str
    age: int
    role: str = "Developer"
    skills: list[str] = field(default_factory=list)

p = Person("Mahoraga", 22, skills=["python", "sql"])

d = asdict(p)
print(d)
# {'name': 'Mahoraga', 'age': 22, 'role': 'Developer', 'skills': ['python', 'sql']}
print(type(d))   # <class 'dict'>


# u can reverse unpack with ** as thus

data = {"name": "Sukuna", "age": 30, "role": "Designer", "skills": ["figma"]}

p2 = Person(**data)
print(p2)
print(p2.name)
print(p2.role)
