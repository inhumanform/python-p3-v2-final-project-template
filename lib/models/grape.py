from models.__init__ import CONN, CURSOR

class Grape:

    all = []

    def __init__(self, grape_id, name, color, key_growing_regions, parentage):
        self.grape_id = grape_id
        self.name = name
        self.color = color
        self.key_growing_regions = key_growing_regions
        self.parentage = parentage
        self.id = None
        
    @property
    def name(self):
        return self._name
    
    @property
    def color(self):
        return self._color
    
    @property
    def key_growing_regions(self):
        return self._key_growing_regions
    
    @property
    def parentage(self):
        return self._parentage

    @classmethod
    def instance_from_db(cls, row):
        grape = cls(row[1])
        grape.id = row[0]
        return grape

    @classmethod
    def get_all_grapes(cls):
        sql = """
            SELECT *
            FROM grapes
        """
        rows = CURSOR.execute(sql).fetchone()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
        SELECT * FROM grapes
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
        SELECT * FROM grapes
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
            FROM grapes
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            print("This ID doesn't exist...")
            return None


        # query = f"SELECT * FROM {'grapes'}"
        # cursor.execute(query)
        # entries = cursor.fetchall()
        # return entries