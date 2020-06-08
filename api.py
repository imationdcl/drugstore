from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from database import Database, SQLITE

dbms = Database(SQLITE, dbname='drugstore.db')
#db_connect = create_engine('sqlite:////drugstore.db') #La ruta depende de donde tengas almacenada la base de datos
#conn = db_connect.connect() # Conexión a la Base de Datos
app = Flask(__name__)

api = Api(app)


class Drugstore(Resource):
    def get(self):

        local_name = request.args.get('local_nombre')
        commune_name = request.args.get('comuna_nombre')
        
        query = 'select local_nombre, local_direccion, local_lat, local_lng from drugstores' # Esta línea ejecuta un query y retorna un json como resultado
        
        if local_name or commune_name != "":
            query += ' where 1=1 '
        
        if local_name != None:
            query += " and local_nombre = '{0}'".format(local_name)

        if commune_name != None:
            query += " and comuna_nombre = '{0}'".format(commune_name)



        result = dbms.select_execute(query=query)
        
        return jsonify({'data': [dict(row) for row in result]})


class DrugstoreData(Resource):
    def get(self, drugstore_id):
        query = "select local_nombre, local_direccion, local_lat, local_lng from drugstores where local_id =%d " % int(drugstore_id)
        result = dbms.select_execute(query=query)
        
        return jsonify({'data': [dict(row) for row in result]})


api.add_resource(Drugstore, '/drugstores')
api.add_resource(DrugstoreData, '/drugstore/<drugstore_id>')

if __name__ == '__main__':
    dbms.create_db_tables()
    dbms.clean_data()
    dbms.load_sample_data()
    app.run(port='5000', debug=True)