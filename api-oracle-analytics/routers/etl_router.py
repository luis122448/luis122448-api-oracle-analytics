from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
import requests
from schemas.elt_schema import EtlBasic, EtlComplex
from schemas.api_response_schema import ApiResponseSchema

etl_router = APIRouter()

@etl_router.post('/erp/oracle-analytics-token',tags=["TEST"], response_model=ApiResponseSchema)
def dwTEST(request_body: EtlBasic):

    # URL de la API REST
    url = 'https://cloud.grupotsiperu.com.pe:8000/erp/test'

    # Realizar la solicitud POST
    response = requests.get(url, verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Devolver los datos como respuesta en formato JSON
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.json())

@etl_router.post('/erp/dataset/dw-cventas-dataset',tags=["CVENTAS"], response_model=ApiResponseSchema)
def dwCVENTASDataset(request_body: EtlComplex):

    # URL de la API REST
    url = 'cloud.grupotsiperu.com.pe:8000/erp/dataset/dw-cxc-dataset'

    # Realizar la solicitud POST
    response = requests.post(url, json=request_body, verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Devolver los datos como respuesta en formato JSON
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.json())
    
@etl_router.post('/erp/dataset/dw-cxc-dataset',tags=["CXC"], response_model=ApiResponseSchema)
def dwCXCDataset(request_body: EtlBasic):

    # URL de la API REST
    url = 'cloud.grupotsiperu.com.pe:8000/erp/dataset/dw-cxc-dataset'

    # Realizar la solicitud POST
    response = requests.post(url, json=request_body, verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Devolver los datos como respuesta en formato JSON
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.json())
