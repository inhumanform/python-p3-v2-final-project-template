#  Here are your defined classes, relating to the tables in your db. 
from models.__init__ import CONN, CURSOR
from models.grape import Grape

class SubRegion:

    all = []

    def __init__(self, name, key_varietals, parent_region, climate):
        self.name = name
        self.key_varietals = key_varietals
        self.parent_region = parent_region
        self.climate = climate
        self.id = None


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)):
            self._name = name_param
        else:
            raise Exception("Subregion name must be a string.")
        
    
    @property
    def key_varietals(self):
        return self._key_varietals
    
    @key_varietals.setter
    def key_growing_regions(self, varietal_param):
        if not isinstance(varietal_param, str):
            raise ValueError("Key growing regions must be a comma-separated string")

    
    valid_grape_names = {grape.name.upper() for grape in Grape.get_all_grapes()}

    varietal_list = varietal_param.strip().split(", ")
    if not varietal_list:
        raise ValueError("Key growing regions cannot be empty")

    invalid_names = [name for name in varietal_list if name.upper() not in valid_grape_names]

    if invalid_names:
        invalid_names_str = ", ".join(invalid_names)
        raise ValueError(f"Invalid grape names: {invalid_names_str}")

# Store the validated list of varietal names (uppercase) in a private attribute
    # self._key_varietals = [name.upper() for name in varietal_list]

    
    @property
    def parent_region(self):
        return self._parent_region
    
    @parent_region.setter
    def parent_region(self, parent_region_param, str):
        if(isinstance(parent_region_param, str)):
            self._parent_region = parent_region_param
        else:
            raise Exception("Growing Region must be a string.")
    
    @property
    def parentage(self):
        return self._parentage
    
    @parentage.setter
    def parentage(self, parentage_param):
        if isinstance(parentage_param, str):
            raise ValueError("Parentage must be a string")

    # Split the string by comma and space, handling potential leading/trailing whitespace
        parentage_list = parentage_param.strip().split(", ")

        if len(parentage_list) != 2:
            raise ValueError("Parentage string must contain exactly two comma-separated names")

    # Validate each name directly using list comprehension and database check
        if any(name.upper() not in [grape.name.upper() for grape in Grape.get_all_grapes()] for name in parentage_list):
            invalid_names = ", ".join([name for name in parentage_list if name.upper() not in [grape.name.upper() for grape in Grape.get_all_grapes()]])
            raise ValueError(f"Parentage names {invalid_names} do not exist in the database")

    # Store the validated parentage (list of strings) in a private attribute
        self._parentage = parentage_list
    
    @classmethod
    def create_table(cls):
        sql = '''
        CREATE TABLE IF NOT EXISTS SubRegion (
        id INTEGER PRIMARY KEY,
        name TEXT,
        key_varietals TEXT,
        FOREIGN KEY (key_varietals) REFERENCES Grape(name)
        parent_region TEXT,
        FOREIGN KEY (parent_region) REFERENCES ParentRegion(name)
                )'''
        CURSOR.execute(sql)
        CONN.commit() 
    
    @classmethod
    def drop_table(cls):
        sql = """
          DROP TABLE IF EXISTS subregion;
        """
        CURSOR.execute(sql)
    
    def save(self):
        sql = """
          INSERT INTO subregion (name) 
          VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Grape.all.append(self)
    
    @classmethod
    def create(cls, name):
        subregion = cls(name)
        subregion.save()
        return subregion

    @classmethod
    def instance_from_db(cls, row):
        subregion = cls(row[1])
        subregion.id = row[0]
        return subregion

    @classmethod
    def get_all_subregions(cls):
        sql = """
            SELECT *
            FROM subregion
        """
        rows = CURSOR.execute(sql).fetchone()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
        SELECT * FROM subregion
        WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("That's not a real thing.")
            return None
        
    @classmethod
    def find_by_region(cls, parent_region):
        sql = """
        SELECT * FROM grapes
        WHERE parent_region = ?
        """
        row = CURSOR.execute(sql, (parent_region)). fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("That's not a real place")
            return None

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT * 
            FROM subregion
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("This ID doesn't exist...")
            return None