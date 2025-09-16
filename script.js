document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('form');
    const errorMessageDiv = document.getElementById('error-mensaje');
    const baseURL = 'http://127.0.0.1:5000'; // Define la URL base

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita el envío del formulario por defecto

        const user = document.getElementById('user').value.trim();
        const password = document.getElementById('password').value.trim();

        errorMessageDiv.textContent = ''; // Limpia cualquier mensaje de error previo

        if (user === '') {
            mostrarError('Por favor, introduce tu nombre de usuario.');
            return;
        }

        if (password === '') {
            mostrarError('Por favor, introduce tu contraseña.');
            return;
        }

        // Aquí podrías agregar más validaciones del lado del cliente si lo deseas

        // Envía los datos al servidor usando Fetch API
        fetch(`${baseURL}/User`, { // Usa la URL base combinada con el endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ // Convierte el objeto a JSON string
                  user: user,
                  password: password,
                }),
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(err.error || 'Error al iniciar sesión.');
                });
            }
            return response.json();
        })
        .then(data => {
            // Redirige al usuario a la página principal o realiza alguna otra acción
            console.log('Inicio de sesión exitoso:', data);
            window.location.href = 'tablas.html'; // Reemplaza '/dashboard' con la URL deseada
        })
        .catch(error => {
            console.error('Error al iniciar sesión:', error);
            mostrarError(error.message);
        });
    });

    function mostrarError(mensaje) {
        errorMessageDiv.textContent = mensaje;
    }
});
