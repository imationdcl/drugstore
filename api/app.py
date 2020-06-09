from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from database import Database, SQLITE

dbms = Database(SQLITE, dbname='drugstore.db')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)


class Drugstore(Resource):
    def get(self):

        local_name = request.args.get('local_nombre')
        commune_id = request.args.get('comuna_id')

        print(local_name)
        
        query = 'select local_nombre, local_direccion, local_telefono, local_lat, local_lng from drugstores' # Esta línea ejecuta un query y retorna un json como resultado
        
        if local_name or commune_id != None:
            query += ' where 1=1 '
        
        if local_name != None and local_name != '':
            query += " and local_nombre = '{0}'".format(local_name)

        if commune_id != None and commune_id != '':
            query += " and fk_comuna = '{0}'".format(commune_id)

        result = dbms.select_execute(query=query)
        
        return jsonify({'data': [dict(row) for row in result]})


class DrugstoreData(Resource):
    def get(self, drugstore_id):
        query = "select local_nombre, local_direccion, local_telefono, local_lat, local_lng from drugstores where local_id =%d " % int(drugstore_id)
        result = dbms.select_execute(query=query)
        
        return jsonify({'data': [dict(row) for row in result]})


api.add_resource(Drugstore, '/drugstores')
api.add_resource(DrugstoreData, '/drugstore/<drugstore_id>')

if __name__ == '__main__':
    dbms.create_db_tables()
    dbms.clean_data()
    dbms.load_sample_data()
    app.run(host='0.0.0.0')