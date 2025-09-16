from base import retrieve_user, check_password
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import Error
# user sign in
app = Flask(__name__)
CORS(app)

@app.route('/User', methods=['POST'])

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
        

if __name__ == "__main__":
    app.run(debug=True)

