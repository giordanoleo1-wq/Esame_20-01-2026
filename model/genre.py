from dataclasses import dataclass
@dataclass
class Genre:
    id: int
    name: str

    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return self.name