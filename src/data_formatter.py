from flask import jsonify

def data_formatter(data):
    return jsonify({'data': data})