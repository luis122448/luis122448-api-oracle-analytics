from fastapi import FastAPI
import requests

app = FastAPI()
app.title = "App Test"
app.version = "1.0.0"

@app.get('/erp/oracle-analytics-token')
def message():

    # URL de la API REST
    url = 'https://sweb3.grupotsiperu.com.pe:8035/erp/api/rest/general/public/oracle-analytics-token'

    # Realizar la solicitud GET
    # response = requests.get(url)

    response = requests.get(url, verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Obtener los datos de la respuesta
        data = response.json()
        # Aquí puedes realizar cualquier manipulación de los datos obtenidos

        # Devolver los datos como respuesta en formato JSON
        return data
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        return 

if __name__ == '__main__':
    app.run()