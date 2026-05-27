cat > /mnt/user-data/outputs/app_complete.py << 'ENDAPP'
from flask import Flask, request, jsonify
import json, os, threading, webbrowser, sys
from datetime import datetime

app = Flask(_name_)

INVENTARIO_FILE = 'inventario.json'
VENTAS_FILE = 'ventas.json'
CUPONES_FILE = 'cupones.json'
TARJETAS_FILE = 'tarjetas.json'
PROVEEDORES_FILE = 'proveedores.json'
MOVIMIENTOS_FILE = 'movimientos.json'
CIERRES_FILE = 'cierres.json'
FACTURAS_FILE = 'facturas.json'

PRODUCTOS_INICIALES = {
    "colchones": [
        {"codigo": "COL001", "nombre": "Colchon Ideal 070", "proveedor": "Josen SAS"},
        {"codigo": "COL002", "nombre": "Colchon Ideal 075", "proveedor": "Josen SAS"},
        {"codigo": "COL003", "nombre": "Colchon Ideal 080", "proveedor": "Josen SAS"},
        {"codigo": "COL004", "nombre": "Colchon Superior 080x14", "proveedor": "Josen SAS"},
    ],
    "sommiers": [
        {"codigo": "SOM001", "nombre": "Sommier Duo Belmo", "proveedor": "Zozzoli SRL"},
        {"codigo": "SOM002", "nombre": "Sommier Duo Multiespace", "proveedor": "Zozzoli SRL"},
    ],
    "almohadas": [{"codigo": "ALM001", "nombre": "Almohada Eterniti", "proveedor": "Zozzoli SRL"}],
    "plasticos": [{"codigo": "PLA001", "nombre": "Plastico Cristal 2x100x100", "proveedor": "Menndogni - Agrimplex"}],
    "silobolsas": [
        {"codigo": "SIL001", "nombre": "Silobolsa 6 pies", "proveedor": "Plastar"},
        {"codigo": "SIL002", "nombre": "Silobolsa 9 pies", "proveedor": "Plastar"},
    ],
    "sogas": [{"codigo": "SOG001", "nombre": "Soga 3mm", "proveedor": "Hilado Esperanza"}],
}

TARJETAS_INICIALES = ['Visa','Mastercard','Cabal','American Express','Naranja','Sol','Su Credito','Credi Cash']
PROVEEDORES_INICIALES = ['Josen SAS','Zozzoli SRL','Menndogni - Agrimplex','Plastar','Hilado Esperanza']

def _load(path, default):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return default

def _save(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def cargar_inventario():
    inv = _load(INVENTARIO_FILE, None)
    if inv is None:
        inv = {cat: [{**p,'stock':0,'stockMinimo':5,'precio':0,'vendidos':0} for p in prods]
               for cat, prods in PRODUCTOS_INICIALES.items()}
        _save(INVENTARIO_FILE, inv)
    return inv

def cargar_tarjetas(): return _load(TARJETAS_FILE, [{'nombre':t,'activa':True} for t in TARJETAS_INICIALES])
def cargar_proveedores(): return _load(PROVEEDORES_FILE, PROVEEDORES_INICIALES)
def cargar_movimientos(): return _load(MOVIMIENTOS_FILE, [])
def cargar_cupones(): return _load(CUPONES_FILE, [])
def cargar_ventas(): return _load(VENTAS_FILE, [])
def cargar_cierres(): return _load(CIERRES_FILE, [])
def cargar_facturas(): return _load(FACTURAS_FILE, [])

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>YUNCO DE FEMO SRL</title><style>
*{margin:0;padding:0;box-sizing:border-box}body{font-family:"Segoe UI",sans-serif;background:linear-gradient(135deg,#1F4E78,#2d5f8f);
min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}.card{background:#fff;border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,.3);
padding:50px;max-width:560px;width:100%;text-align:center}h1{color:#1F4E78;font-size:32px;margin-bottom:8px}
p{color:#666;margin-bottom:36px}.btn{display:block;padding:18px;font-size:17px;font-weight:600;border-radius:10px;
color:#fff;text-decoration:none;margin-bottom:16px;transition:.3s}.btn:hover{transform:translateY(-3px);opacity:.92}
.b1{background:linear-gradient(135deg,#1F4E78,#2d7fba)}.b2{background:linear-gradient(135deg,#28a745,#20c997)}
.b3{background:linear-gradient(135deg,#e67e22,#f39c12)}
</style></head><body><div class="card"><h1>YUNCO DE FEMO SRL</h1><p>Sistema Profesional de Gestion</p>
<a href="/inventario" class="btn b1">Inventario y Ventas</a>
<a href="/cupones" class="btn b2">Cupones de Tarjeta</a>
<a href="/caja" class="btn b3">Cierre de Caja</a>
</div></body></html>'''

@app.route('/inventario')
def inventario(): return '<h1>Inventario - En Construccion</h1><a href="/">Volver</a>'

@app.route('/cupones')
def cupones(): return '<h1>Cupones - En Construccion</h1><a href="/">Volver</a>'

@app.route('/caja')
def caja(): return '<h1>Cierre de Caja - En Construccion</h1><a href="/">Volver</a>'

@app.route('/api/inventario', methods=['GET'])
def get_inventario(): return jsonify(cargar_inventario())
@app.route('/api/inventario', methods=['POST'])
def post_inventario(): _save(INVENTARIO_FILE, request.json); return jsonify({'success': True})

@app.route('/api/tarjetas', methods=['GET'])
def get_tarjetas(): return jsonify(cargar_tarjetas())
@app.route('/api/tarjetas', methods=['POST'])
def post_tarjetas(): _save(TARJETAS_FILE, request.json); return jsonify({'success': True})

@app.route('/api/proveedores', methods=['GET'])
def get_proveedores(): return jsonify(cargar_proveedores())
@app.route('/api/proveedores', methods=['POST'])
def post_proveedores(): _save(PROVEEDORES_FILE, request.json); return jsonify({'success': True})

@app.route('/api/movimientos', methods=['GET'])
def get_movimientos(): return jsonify(cargar_movimientos())
@app.route('/api/movimientos', methods=['POST'])
def post_movimientos(): _save(MOVIMIENTOS_FILE, request.json); return jsonify({'success': True})

@app.route('/api/cupones', methods=['GET'])
def get_cupones(): return jsonify(cargar_cupones())
@app.route('/api/cupones', methods=['POST'])
def post_cupones(): _save(CUPONES_FILE, request.json); return jsonify({'success': True})

@app.route('/api/facturas', methods=['GET'])
def get_facturas(): return jsonify(cargar_facturas())
@app.route('/api/facturas', methods=['POST'])
def post_facturas(): _save(FACTURAS_FILE, request.json); return jsonify({'success': True})

@app.route('/api/cierres', methods=['GET'])
def get_cierres(): return jsonify(cargar_cierres())
@app.route('/api/cierres', methods=['POST'])
def post_cierres(): _save(CIERRES_FILE, request.json); return jsonify({'success': True})

if _name_ == '_main_':
    PORT = int(os.environ.get('PORT', 5000))
    HOST = os.environ.get('HOST', '127.0.0.1')
    if getattr(sys, 'frozen', False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(_file_))
    os.chdir(BASE_DIR)
    print("YUNCO DE FEMO SRL - Sistema de Gestion")
    print("Corriendo en http://"+HOST+":"+str(PORT))
    app.run(host=HOST, port=PORT, debug=False)
ENDAPP
echo "Done"
{
  "returncode" : 0,
  "stdout" : "Done\n",
  "stderr" : ""