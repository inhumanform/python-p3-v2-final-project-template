from models.__init__ import CONN, CURSOR


class ParentRegion:
    def __init__(self, name, climate):
        self.name = name
        self.climate = climate

    @classmethod
    def from_dict(cls, region_dict):
        return cls(**region_dict)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
