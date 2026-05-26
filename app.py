from flask import Flask, request, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)

INVENTARIO_FILE = 'inventario.json'

def _load(path, default):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return default

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html><head><title>YUNCO</title></head><body>
<h1>YUNCO DE FEMO SRL</h1><p>Sistema funcionando!</p>
</body></html>'''

@app.route('/test')
def test():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
