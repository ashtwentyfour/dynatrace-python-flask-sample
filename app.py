"""
Flask sample application
"""

import random

from flask import Flask, jsonify
from utils.logger import get_logger

app = Flask(__name__)

logger = get_logger('default')

@app.route('/hello')
def generate_error():
    """Random Response"""
    random_health = random.randint(0,2)
    if random_health == 0:
        logger.info("hello world!")
        return jsonify({
            "message": "hello"
        }), 200
    if random_health == 1:
        logger.error("404 not found")
        return jsonify({
            "message": "not found"
        }), 404
    logger.error("502 unavailable")
    return jsonify({
        "message": "service unavailable"
    }), 502

@app.route('/health')
def health_check():
    """Health Check"""
    return jsonify({
        "status": "UP"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
