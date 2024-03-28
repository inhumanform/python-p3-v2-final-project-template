from models.grape import Grape
from models.subregion import SubRegion
from models.parentregion import ParentRegion
from models.__init__ import CONN, CURSOR

if __name__ == "__main__":
    Grape.create_table()
    SubRegion.create_table()
    ParentRegion.create_table()

    CURSOR.execute("DELETE FROM grape")
    CURSOR.execute("DELETE FROM subregion")
    CONN.commit()

    Grape.create("Chardonnay", "White", "Chablis, Napa Valley", "Pinot, Gouais")
    Grape.create("Cabernet Sauvignon", "Red", "Napa Valley, Medoc", "Cabernet Franc, Sauvignon Blanc")
    Grape.create("Pinot Noir", "Red", "Cote d'Or, Willamette Valley", "OG")

    SubRegion.create("Cote d'Or", "Chardonnay, Pinot Noir, Aligote, Pinot Blanc" "Burgundy", "Temperate")
    SubRegion.create("Napa Valley", "Cabernet Sauvignon, Chardonnay, Zinfandel, Sauvignon Blanc", "California" "Mediterranean")
    SubRegion.create("Saar", "Riesling", "Mosel", "Continental" )
    SubRegion.create("Willamete Valley", "Cabernet Franc, Pinot Noir", "Oregon", "Maritime")

    ParentRegion.create("Burgundy", "France")
    ParentRegion.create("Mosel", "Germany")
    ParentRegion.create("California", "USA")
    ParentRegion.create("Oregon", "USA")
    ParentRegion.create("Bordeaux", "France")
    ParentRegion.create("Piedmonte", "Italy")