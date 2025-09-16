from base import hash_password, store_user
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

@app.route('/New', methods=['POST'])
# user log in
def Ne_user():
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
    
if __name__ == "__main__":
    app.run(debug=True)




