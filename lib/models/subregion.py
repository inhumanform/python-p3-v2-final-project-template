#  Here are your defined classes, relating to the tables in your db. 
from models.__init__ import CONN, CURSOR

class SubRegion:
    def __init__(self, name, main_varietals, parent_region, climate):
        self.name = name
        self.main_varietals = main_varietals
        self.parent_region = parent_region
        self.climate = climate
