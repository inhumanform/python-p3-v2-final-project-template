#  Here are your defined classes, relating to the tables in your db. 

class Wine:
    def __init__(self, name, color, key_growing_regions, parentage):
        self.name = name
        self.color = color
        self.key_growing_regions = key_growing_regions
        self.parentage = parentage

class Region:
    def __init__(self, name, climate):
        self.name = name
        self.climate = climate

class Subregion:
    def __init__(self, name, main_varietals, parent_region, climate):
        self.name = name
        self.main_varietals = main_varietals
        self.parent_region = parent_region
        self.climate = climate