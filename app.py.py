from flask import Flask, request, jsonify
import json, os, threading, webbrowser, sys
from datetime import datetime

app = Flask(_name_)

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

if _name_ == '_main_':
    app.run(host='127.0.0.1', port=5000, debug=False)
    cat > /mnt/user-data/outputs/app_simple.py << 'ENDPY'
from flask import Flask, request, jsonify
import json, os

app = Flask(_name_)

@app.route('/')
def index():
    return '<h1>YUNCO funcionando!</h1>'

@app.route('/test')
def test():
    return jsonify({'status': 'ok'})

if _name_ == '_main_':
    app.run(host='127.0.0.1', port=5000)
ENDPY
echo "Done"
{
  "returncode" : 0,
  "stdout" : "Done\n",
  "stderr" : ""