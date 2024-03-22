from flask import jsonify

def output_formatter(data):
    return jsonify({'data': data})