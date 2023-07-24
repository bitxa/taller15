import csv
import requests

BASE_URL = "http://127.0.0.1:8000/api/"
USERNAME = "sebastian"
PASSWORD = "sebastian"

propietarios = []
edificios = []
departamentos = []

edificios_data = []
propietarios_data = []


def cargar_datos_desde_csv(nombre_archivo):
    ruta_archivo = f"data/{nombre_archivo}"
    with open(ruta_archivo, newline='', encoding='utf-8', ) as csvfile:
        return list(csv.DictReader(csvfile, delimiter='|'))


def post(url, data):
    response = requests.post(url, json=data, auth=(USERNAME, PASSWORD))
    return response


def crear_propietario(datos):
    url = BASE_URL + "propietarios/"
    propietario_data = {
        "nombre": datos.get("nombre"),
        "apellido": datos.get("apellido"),
        "cedula": datos.get("cedula")
    }
    response = post(url, propietario_data)
    if response.status_code == 201:
        print(
            f"Propietario '{datos.get('Nombre')} {datos.get('Apellido')}' creado exitosamente.")
    else:
        print(
            f"Error al crear el propietario '{datos.get('Nombre')} {datos.get('Apellido')}': {response.text}")


def crear_edificio(datos):
    url = BASE_URL + "edificios/"
    edificio_data = {
        "nombre": datos.get("nombre"),
        "direccion": datos.get("dirección"),
        "ciudad": datos.get("ciudad"),
        "tipo": datos.get("tipo")
    }

    response = post(url, edificio_data)
    if response.status_code == 201:
        print(f"Edificio '{datos.get('nombre')}' creado exitosamente.")
    else:
        print(
            f"Error al crear el edificio '{datos.get('nombre')}': {response.text}")


def crear_departamento(datos):
    url = BASE_URL + "departamentos/"
    departamento_data = {
        "propietario": get_propietario_for_departamento(datos.get("Propietario")),
        "costo": datos.get("Costo"),
        "num_cuartos": datos.get("Cuartos"),
        "edificio": get_propietario_for_departamento(datos.get("Edificio")),
    }

    response = post(url, departamento_data)
    if response.status_code == 201:
        print(
            f"Departamento en el edificio '{datos['edificio']}' creado exitosamente.")
    else:
        print(
            f"Error al crear el departamento en el edificio '{datos['Edificio']}': {response.text}")


def cargar_propietarios():
    global propietarios
    propietarios = cargar_datos_desde_csv("propietarios.csv")


def cargar_edificios():
    global edificios
    edificios = cargar_datos_desde_csv("edificios.csv")


def cargar_departamentos():
    global departamentos
    departamentos = cargar_datos_desde_csv("departamentos.csv")


def upload_propietarios():
    for propietario in propietarios:
        crear_propietario(propietario)


def upload_edificios():
    for edificio in edificios:
        crear_edificio(edificio)


def upload_departamentos():
    for departamento in departamentos:
        crear_departamento(departamento)


def get_propietario_for_departamento(cedula):
    for propietario in propietarios_data:
        if propietario.get("cedula") == cedula:
            return propietario


def get_edificio_for_departamento(nombre):
    for edificio in edificios_data:
        if edificio.get("nombre") == nombre:
            return edificio


def get_all_edificios():
    edificios_data = requests.get(BASE_URL + "edificios/").json()


def get_all_propietarios():
    propietarios_data = requests.get(BASE_URL + "propietarios/").json()


def main():
    cargar_propietarios()
    cargar_edificios()
    cargar_departamentos()

    get_all_propietarios()
    get_all_edificios()

    upload_propietarios()
    upload_edificios()
    upload_departamentos()


if __name__ == "__main__":
    main()
