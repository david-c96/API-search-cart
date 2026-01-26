from base import retrieve_user, check_password
from base import hash_password, store_user, general_search
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import Error
# -------------------------------------------
#  REGISTRO DE USUARIO
# -------------------------------------------
app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])

def main():
    try:
        data = request.get_json()
        user = data.get("user")
        password = data.get("password")

        if user is None or password is None:
            return jsonify({'error': 'Debes proporcionar "user" y "password" en el cuerpo de la solicitud JSON.'}), 400
        
        if not isinstance(user, (str)) or not isinstance(password, (str)):
            return jsonify({'error': '"user" y "password" deben ser cadenas de texto.'}), 400 
        
        stored_hash = retrieve_user(user)
        if stored_hash is None:
            return jsonify({'error': f'El usuario "{user}" no existe.'}), 404
        
        if check_password(stored_hash, password):
            return jsonify({'message': f'Contraseña del usuario "{user}" es correcta.'}), 200
        else:
            return jsonify({'error': 'Credenciales inválidas.'}), 401
        
    except Error as e:
        return jsonify({'error': f'El usuario "{user}" o la contraseña ya existe.'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        

# -------------------------------------------
#  INICIO DE SESIÓN
# -------------------------------------------
@app.route('/register', methods=['POST'])

def New():
    try:
        data = request.get_json()
        user = data.get("user")
        password = data.get("password")

        if user is None or password is None:
            return jsonify({'error': 'Debes proporcionar "user" y "password" en el cuerpo de la solicitud JSON.'}), 400

        if not isinstance(user, (str)) or not isinstance(password, (str)):
            return jsonify({'error': '"user" y "password" deben ser cadenas de texto.'}), 400 
        
        hashed = hash_password(password)
# Almacena el usuario
        store_user(user, hashed)
        return jsonify({'message': f'Usuario "{user}" registrado exitosamente.'}), 201
    
    except Error as e:
        return jsonify({'error': f'El usuario "{user}" ya existe.'}), 409

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/search", methods=["POST"])
def buscar():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar un JSON."}), 400

    result = general_search(data)

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)

