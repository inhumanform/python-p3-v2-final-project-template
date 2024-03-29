from models.__init__ import CONN, CURSOR
import ipdb

class Grape:

    all = []

    def __init__(self, name, color, key_growing_regions, parentage):
        self.name = name
        self.color = color
        # ipdb.set_trace()
        self.key_growing_regions = key_growing_regions
        self.parentage = parentage
        self.id = None
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)):
            # ipdb.set_trace()
            self._name = name_param
        else:
            raise Exception("Grape names must be a string.")
        
    # def __repr__(self):
    #     return f"<Grape {self.id}: Name = {self.name}, Color = {self.color}, Key Growing Regions = {self.key_growing_regions}, Parentage = {self.parentage}>"
    
    @classmethod
    def create_table(cls):
        sql = """
          CREATE TABLE IF NOT EXISTS grape (
          id INTEGER PRIMARY KEY,
          name TEXT,
          color TEXT
          )"""
        CURSOR.execute(sql)
        # CONN.commit()
        print("Data added successfully.") 
        
    
    @classmethod
    def instance_from_db(cls, row):
        grape = cls(row[1])
        grape.id = row[0]
        return grape
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color_param):
        if not isinstance(color_param, str) or color_param.upper() not in ("RED", "WHITE", "GRIS"):
            # ipdb.set_trace()
            raise ValueError(f"Color must be one of 'Red', 'White', or 'Gris' (case-insensitive)")

    
    @property
    def key_growing_regions(self):
        return self._key_growing_regions
    
    @key_growing_regions.setter
    def key_growing_regions(self, key_growing_regions_param, str):
        if(isinstance(key_growing_regions_param, str)):
            # ipdb.set_trace()
            self._key_growing_regions = key_growing_regions_param
        else:
            raise Exception("Growing Region must be a string.")
    
    @property
    def parentage(self):
        return self._parentage
    
    @parentage.setter
    def parentage(self, parentage_param):
        if isinstance(parentage_param, str):
            # ipdb.set_trace()
            raise ValueError("Parentage must be a string")

    # Split the string by comma and space, handling extra spaces
        parentage_list = parentage_param.strip().split(", ")

        if len(parentage_list) != 2:
            raise ValueError("Parentage string must contain exactly two comma-separated names")

        if any(name.upper() not in [grape.name.upper() for grape in Grape.get_all_grapes()] for name in parentage_list):
            invalid_names = ", ".join([name for name in parentage_list if name.upper() not in [grape.name.upper() for grape in Grape.get_all_grapes()]])
            raise ValueError(f"Parentage names {invalid_names} do not exist in the database")

   
        self._parentage = parentage_list
    
    @classmethod
    def drop_table(cls):
        sql = """
          DROP TABLE IF EXISTS grape;
        """
        CURSOR.execute(sql)
    
    def save(self):
        sql = """
          INSERT INTO grape (name, color, key_growing_regions) 
          VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.color, self.key_growing_regions))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Grape.all.append(self)
    
    @classmethod
    def create(cls, name, color, key_growing_regions, parentage):
        grape = cls(name, color, key_growing_regions, parentage)
        grape.save()
        return grape

    @classmethod
    def instance_from_db(cls, row):
        grape = cls(row[1])
        grape.id = row[0]
        return grape

    @classmethod
    def get_all_grapes(cls):
        sql = """
            SELECT *
            FROM grape
        """
        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
        SELECT * FROM grape
        WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("That's not a real thing.")
            return None
        
    @classmethod
    def find_by_region(cls, key_growing_regions):
        sql = """
        SELECT * FROM grape
        WHERE key_growing_regions = ?
        """
        row = CURSOR.execute(sql, (key_growing_regions)). fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("That's not a real place")
            return None

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT * 
            FROM grape
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("This ID doesn't exist...")
            return None