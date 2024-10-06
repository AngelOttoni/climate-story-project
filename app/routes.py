from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/co2data', methods=['GET'])
def get_co2_data():
    data = {'message': "CO2 data will be here"}
    return jsonify(data)

#app/routes.py