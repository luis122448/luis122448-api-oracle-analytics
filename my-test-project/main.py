from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn
import os
import base64
import ssl

app = FastAPI()
app.title = "App Test"
app.version = "1.0.0"

class UsuarioAuthConfig(BaseModel):
    ruc: str
    coduser: str
    clave: str

@app.get('/erp/oracle-analytics-token')
def oracleAnalyticsToken():

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
        return {"error": "Error al realizar la solicitud GET"}

@app.post('/erp/auth-config')
def authConfig(usuario: UsuarioAuthConfig):

    # URL de la API REST
    url = 'https://sweb3.grupotsiperu.com.pe:8035/erp/api/rest/usuario/auth-config'

    # Decodificar la clave en base64
    clave = usuario.clave
    # clave = base64.b64decode(usuario.clave).decode('utf-8')

    # Datos del JSON a enviar
    data = {
        "ruc": usuario.ruc,
        "coduser": usuario.coduser,
        "clave": clave
    }

    # Ruta al archivo del certificado
    cert_file = "./_.grupotsiperu.com.pe.crt"

    # with open(cert_file, "r") as file:
    #     content = file.read()
    #     print(content)
    # Crear un contexto SSL con el certificado
    # context = ssl.create_default_context(cafile=cert_file)

    # Realizar la solicitud POST
    response = requests.post(url, json=data, verify=cert_file)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Obtener los datos de la respuesta
        result = response.json()
        # Aquí puedes realizar cualquier manipulación de los datos obtenidos

        # Devolver los datos como respuesta en formato JSON
        return result
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        return {"error": "Error al realizar la solicitud POST"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))
    app.run()