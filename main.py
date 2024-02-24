from flask import Flask, jsonify, request
from db_connector import CarDatabase

app = Flask(__name__)

car_db = CarDatabase()

@app.route('/selected_columns', methods=['GET'])
def get_selected_columns():
    columns = request.args.get('columns', default='make,model,year,price', type=str).split(',')
    data = car_db.get_selected_columns(columns)
    return jsonify(data)

@app.route('/filtered_data/<string:condition>', methods=['GET'])
def get_filtered_data(condition):
    data = car_db.get_filtered_data(condition)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
