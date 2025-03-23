from base import hash_password, store_user

# user log in
def main():
    usre = "david96"
    password = "david96"
    
    # Hashea la contraseña
    hashed = hash_password(password)
    
    # Almacena el usuario
    store_user(usre, hashed)
    
    # Verifica el usuario
if __name__ == "__main__":
    main()




