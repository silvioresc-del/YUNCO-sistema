cat > /mnt/user-data/outputs/app_final.py << 'FINAL'
from flask import Flask
import os, sys

app = Flask(_name_)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YUNCO DE FEMO SRL</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: "Segoe UI", sans-serif;
            background: linear-gradient(135deg, #1F4E78, #2d5f8f);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .card {
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,.3);
            padding: 50px;
            max-width: 560px;
            width: 100%;
            text-align: center;
        }
        h1 { color: #1F4E78; font-size: 32px; margin-bottom: 8px; }
        p { color: #666; margin-bottom: 36px; }
        .btn {
            display: block;
            padding: 18px;
            font-size: 17px;
            font-weight: 600;
            border-radius: 10px;
            color: #fff;
            text-decoration: none;
            margin-bottom: 16px;
            transition: .3s;
        }
        .btn:hover { transform: translateY(-3px); opacity: .92; }
        .b1 { background: linear-gradient(135deg, #1F4E78, #2d7fba); }
        .b2 { background: linear-gradient(135deg, #28a745, #20c997); }
        .b3 { background: linear-gradient(135deg, #e67e22, #f39c12); }
    </style>
</head>
<body>
    <div class="card">
        <h1>YUNCO DE FEMO SRL</h1>
        <p>Sistema Profesional de Gestion</p>
        <a href="/inventario" class="btn b1">Inventario y Ventas</a>
        <a href="/cupones" class="btn b2">Cupones de Tarjeta</a>
        <a href="/caja" class="btn b3">Cierre de Caja</a>
    </div>
</body>
</html>'''

@app.route('/inventario')
def inventario():
    return '<h1>Inventario</h1><p>Modulo en desarrollo</p><a href="/">Volver</a>'

@app.route('/cupones')
def cupones():
    return '<h1>Cupones</h1><p>Modulo en desarrollo</p><a href="/">Volver</a>'

@app.route('/caja')
def caja():
    return '<h1>Cierre de Caja</h1><p>Modulo en desarrollo</p><a href="/">Volver</a>'

if _name_ == '_main_':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
FINAL
echo "Listo"