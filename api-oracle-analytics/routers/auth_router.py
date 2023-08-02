from fastapi import HTTPException, status, APIRouter
import requests
from schemas.auth_schema import UsuarioAuthConfig

auth_router = APIRouter()

@auth_router.get('/erp/oracle-analytics-token',tags=["AUTH"])
def oracleAnalyticsToken():

    # URL de la API REST
    url = 'https://sweb3.grupotsiperu.com.pe:8835/erp/api/rest/general/public/oracle-analytics-token'

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

@auth_router.post('/erp/auth-analytics',tags=["AUTH"])
def authConfig(usuario: UsuarioAuthConfig):

    # URL de la API REST
    url = 'https://sweb3.grupotsiperu.com.pe:8835/erp/api/rest/usuario/auth-analytics'

    # Datos del JSON a enviar
    data = {
        "ruc": usuario.ruc,
        "coduser": usuario.coduser,
        "clave": usuario.clave
    }

    # Realizar la solicitud POST
    response = requests.post(url, json=data, verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Obtener los datos de la respuesta
        result = response.json()
        # Aquí puedes realizar cualquier manipulación de los datos obtenidos

        # Devolver los datos como respuesta en formato JSON
        return result
    else:
        print(response)
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error al realizar la solicitud POST")
