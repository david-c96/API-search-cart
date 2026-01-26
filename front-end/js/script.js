document.addEventListener('DOMContentLoaded', () => {

// inicio de sesión -------------------------------------

    const loginForm = document.querySelector('#login-form');
    const loginMessageDiv = document.getElementById('login-error');

    if (!loginForm) {
        console.error('No se encontró el formulario de login');
        return;
    }

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        // Obtener valores
        const user = document.getElementById('user').value.trim();
        const password = document.getElementById('password').value.trim();

        // Limpia mensaje de error
        loginMessageDiv.textContent = '';

        // Validación básica
        if (!user || !password) {
            mostrarError('Por favor completa todos los campos.');
            return;
        }

        try {
            const response = await fetch(`http://127.0.0.1:5000/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user: user,
                    password: password,
                }),
            });

            const data = await response.json();

            if (!response.ok) {
                // Si el servidor devuelve error, se muestra el mensaje
                throw new Error(data.error || 'Error al iniciar sesión.');
            }

            console.log('Inicio de sesión exitoso:', data);
            showSection('inicio');

        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            mostrarError(error.message);
        }
    });

        function mostrarError(mensaje) {
        loginMessageDiv.textContent = mensaje;
        loginMessageDiv.style.color = 'red';
        }



//  registro de usuario -------------------------------------


    const registerForm = document.querySelector('#register-form');
    const registerErrorDiv = document.getElementById('register-error');

    if (!registerForm) {
        console.error('No se encontró el formulario de login');
        return;
    }

    registerForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        // Obtener valores
        const user = document.getElementById('Newuser').value.trim();
        const password = document.getElementById('Newpassword').value.trim();

        // Limpia mensaje de error
        registerErrorDiv.textContent = '';

        // Validación básica
        if (!user || !password) {
            mostrarError('Por favor completa todos los campos.');
            return;
        }

        try {
            const response = await fetch(`http://127.0.0.1:5000/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user: user,
                    password: password,
                }),
            });

            const data = await response.json();

            if (!response.ok) {
                // Si el servidor devuelve error, se muestra el mensaje
                throw new Error(data.error || 'Error al iniciar sesión.');
            }

            console.log('Inicio de sesión exitoso:', data);
            window.location.href = 'tablas.html';

        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            mostrarError(error.message);
        }
    });

    function mostrarError(mensaje) {
    registerErrorDiv.textContent = mensaje;
    registerErrorDiv.style.color = 'black';
    }

});

// -------nuevo verificacion de datos y búsqueda en tabla ---------
document.addEventListener("DOMContentLoaded", () => {
    loadData(); // cargar todo
});

// Esta función se ejecuta cuando el usuario escribe en el buscador
function searchData() {
    let searchValue = document.getElementById("searchBox").value;

    // Si está vacío, limpia la tabla
    if (searchValue.trim() === "") {
        document.getElementById("data-body").innerHTML = "";
        return;
    }

    fetch("http://127.0.0.1:5000/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: searchValue })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Datos recibidos:", data);
        loadTable(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}


// Pinta los datos dentro de la tabla
function loadTable(data) {
    const tableBody = document.getElementById("data-body");
    tableBody.innerHTML = ""; // limpiar antes de rellenar

    if (!data || data.length === 0) {
        tableBody.innerHTML = `
            <tr>
                <td colspan="7" style="text-align:center;">No se encontraron resultados</td>
            </tr>
        `;
        return;
    }

    data.forEach(item => {
        let row = `
            <tr>
                <td>${item.model || ""}</td>
                <td>${item.part || ""}</td>
                <td>${item.serial || ""}</td>
                <td>${item.car || ""}</td>
                <td>${item.year || ""}</td>
                <td>${item.color || ""}</td>
                <td>${item.version || ""}</td>
            </tr>
        `;

        tableBody.innerHTML += row;
    });
}

