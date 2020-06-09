from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

import requests

# Global Variables
SQLITE  = 'sqlite'

# Table Name
DRUGSTORE = 'drugstores'

class Database:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    db_engine = None
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")

#print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        Table(DRUGSTORE, metadata,
                      Column('local_id', Integer, primary_key=True),
                      Column('fecha', String),
                      Column('local_nombre', String),
                      Column('comuna_nombre', String),
                      Column('localidad_nombre', String),
                      Column('local_direccion', String),
                      Column('funcionamiento_hora_apertura', String),
                      Column('funcionamiento_hora_cierre', String),
                      Column('local_telefono', String),
                      Column('local_lat', String),
                      Column('local_lng', String),
                      Column('funcionamiento_dia', String),
                      Column('fk_region', String),
                      Column('fk_comuna', String)
                      )
        try:
            metadata.create_all(self.db_engine)
            print("Table created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)


    #Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '' : return
        #print (query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
                return result
            except Exception as e:
                print(e)
    
    def select_execute(self, table='', query=''):
        data = []
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    data.append(row) #print(row) # print(row[0], row[1], row[2])
                result.close()
        return data

    def clean_data(self):
        # Delete all Data
        query = "DELETE FROM {}".format(DRUGSTORE)
        self.execute_query(query)
    
    def load_sample_data(self):
        # Insert Data
        url = "https://farmanet.minsal.cl/maps/index.php/ws/getLocalesRegion?id_region=7"
        response = requests.get(url)

        for drugstore in response.json():
            local_id = drugstore['local_id']
            fecha = drugstore['fecha']
            local_nombre = drugstore['local_nombre'].replace("'", "")
            comuna_nombre = drugstore['comuna_nombre']
            localidad_nombre = drugstore['localidad_nombre']
            local_direccion = drugstore['local_direccion'].replace("'", "")
            funcionamiento_hora_apertura = drugstore['funcionamiento_hora_apertura']
            funcionamiento_hora_cierre = drugstore['funcionamiento_hora_cierre']
            local_telefono = drugstore['local_telefono']
            local_lat = drugstore['local_lat']
            local_lng = drugstore['local_lng']
            funcionamiento_dia = drugstore['funcionamiento_dia']
            fk_region = drugstore['fk_region']
            fk_comuna = drugstore['fk_comuna']
            
            query = "insert into drugstores values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', '{13}')".format(local_id, fecha, local_nombre, comuna_nombre, localidad_nombre, local_direccion,funcionamiento_hora_apertura, funcionamiento_hora_cierre, local_telefono, local_lat, local_lng, funcionamiento_dia,fk_region, fk_comuna)
            self.execute_query(query)
        
        return {'status': 'Drustores added'} 