from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import os
import sys
import logging

# ============================================
# CONFIGURACIÓN
# ============================================
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
CORS(app)

# ============================================
# RUTAS PRINCIPALES
# ============================================

@app.route('/')
def index():
    return redirect(url_for('login_page'))

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/verificar')
def verificar_page():
    return render_template('verificar.html')

@app.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@app.route('/negocio/inventario')
def negocio_inventario():
    return render_template('negocio/inventario.html')

@app.route('/negocio/tienda')
def negocio_tienda():
    return render_template('negocio/tienda.html')

@app.route('/negocio/trabajadores')
def negocio_trabajadores():
    return render_template('negocio/trabajadores.html')

@app.route('/negocio/servicios')
def negocio_servicios():
    return render_template('negocio/servicios.html')

@app.route('/negocio/ventas')
def negocio_ventas():
    return render_template('negocio/ventas.html')

@app.route('/negocio/contratos')
def negocio_contratos():
    return render_template('negocio/contratos.html')

@app.route('/negocio/nomina')
def negocio_nomina():
    return render_template('negocio/nomina.html')

@app.route('/negocio/mapa')
def negocio_mapa():
    return render_template('negocio/mapa.html')

@app.route('/perfil')
def perfil_page():
    return render_template('perfil.html')

@app.route('/admin/db')
def admin_db():
    return render_template('admin/db_manager.html')

# ============================================
# INICIO DE LA APLICACIÓN
# ============================================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
