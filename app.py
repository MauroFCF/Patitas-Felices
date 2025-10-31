from flask import Flask, request, redirect
import mysql.connector

# Inicialización de la aplicación Flask
app = Flask(__name__)

# --- Configuración de la Base de Datos ---
# !!! IMPORTANTE: REEMPLAZA ESTOS VALORES CON TUS CREDENCIALES REALES DE MySQL !!!
DB_CONFIG = {
    'host': 'localhost',
    'user': 'tu_usuario_mysql',      
    'password': 'tu_contraseña_mysql',
    'database': 'Patitas_Felices' # Asegúrate de que esta base de datos exista
}

def get_db_connection():
    """Establece y retorna la conexión a la base de datos."""
    # La conexión usará la configuración definida arriba
    return mysql.connector.connect(**DB_CONFIG)

# ------------------------------------------------------------------
# RUTA PRINCIPAL: Procesar el Formulario de Adopción (Insertar datos)
# ------------------------------------------------------------------
@app.route('/procesar_adopcion', methods=['POST'])
def procesar_adopcion():
    """Recibe los datos del formulario de adopción y los inserta en la tabla 'adopciones'."""
    
    try:
        # 1. Obtener los datos del formulario (usando request.form)
        # Los nombres de las claves deben coincidir con los IDs/nombres de los campos en el HTML
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mascota = request.form.get('mascota')
        motivo = request.form.get('motivo')

        # 2. Conectar a la Base de Datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # 3. Preparar y ejecutar la consulta SQL (usando %s como placeholders)
        sql = "INSERT INTO adopciones (nombre, email, mascota, motivo) VALUES (%s, %s, %s, %s)"
        data = (nombre, email, mascota, motivo)
        
        cursor.execute(sql, data)
        conn.commit() # Confirmar la inserción

        cursor.close()
        conn.close()

        # 4. Mensaje de éxito y redirección
        # Podrías redireccionar al usuario a una página de agradecimiento
        return redirect('/adopciones.html')
    
    except mysql.connector.Error as err:
        # Manejo de errores de la base de datos
        return f"<h1>Error de Base de Datos:</h1><p>No se pudo guardar la solicitud. Detalle: {err}</p>", 500
    except Exception as e:
        # Manejo de otros errores (ej. formulario incompleto)
        return f"<h1>Ocurrió un error inesperado:</h1><p>{e}</p>", 500

# ------------------------------------------------------------------
# Ruta auxiliar para servir archivos estáticos (HTML, CSS, etc.)
# ------------------------------------------------------------------
# Esto permite que tu navegador acceda a archivos como Formulario de adopcion.html
@app.route('/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    # Para ejecutar la aplicación:
    # 1. Crea una carpeta llamada 'static'
    # 2. Mueve tus archivos HTML, CSS, etc., dentro de 'static'
    # 3. Ejecuta este script con 'python app.py'
    app.run(debug=True)
