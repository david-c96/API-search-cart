from base import retrieve_user, check_password
from base import insert, search
from base import eliminate

# user sign in
def main():

    usre = "david96"
    password = "david96"
    
    stored_hash = retrieve_user(usre)
    if stored_hash:
        is_correct = check_password(stored_hash, password)
        print("Contraseña correcta:", is_correct)
    else:
        print("No se pudo verificar la contraseña.")
if __name__ == "__main__":
    main()

# insert part
a = input("Model: ")
b = input("Part: ")
c = input("Serial: ")
d = input("Car: ")
e = input("Year: ")
f = input("Color: ")
g = input("Version: ")

def main():

    model = a
    part = b
    serial = c
    car = d
    year = e
    color = f
    version = g

    insert(model, part, serial, car, year, color, version)
if __name__ == "__main__":
    main()

# search for model
a = input("inserte un modelo: ")

def main():
    model = a 

    search(model)
if __name__ == "__main__":
    main()

a = input("Numero de serial que deseas eliminar: ")

def main():
    eliminates = a

    eliminate(eliminates)
if __name__ == "__main__":
    main()

