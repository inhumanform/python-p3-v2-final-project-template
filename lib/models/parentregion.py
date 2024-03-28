from models.__init__ import CONN, CURSOR


class ParentRegion:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)):
            self._name = name_param
        else:
            raise Exception("Region name must be a string.")
        
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, country_param):
        if(isinstance(country_param, str)):
            self._country = country_param
        else:
            raise Exception("Country must be a string")
        
    def __repr__(self):
        return f"<Region ID #{self.id}| Region Name: {self.name}, Country: {self.country} >"
    
    @classmethod
    def create_table(cls):

        sql="""
            CREATE TABLE IF NOT EXISTS parent_region (
            id INTEGER PRIMARY KEY,
            name TEXT,
            country TEXT)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        
        sql = """
            DROP TABLE IF EXISTS parentregion;
        """
        CURSOR.execute(sql)

    def save(self):

        sql = """
            INSERT INTO parentregion (name, country)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.country,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        ParentRegion.all.append(self)

    @classmethod
    def create(cls, name, country):

        parentregion = cls(name, country)
        parentregion.save()
        return parentregion
    
    @classmethod
    def instance_from_db(cls, row):
        parentregion = cls(row[1], row[2])
        parentregion.id = row[0]
        return parentregion
    
    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM parent_region
        """
        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all