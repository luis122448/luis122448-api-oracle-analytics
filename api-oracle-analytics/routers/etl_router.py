from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import requests
from schemas.elt_schema import EtlBasic, EtlComplex
from schemas.api_response_schema import ApiResponseSchema
import time

etl_router = APIRouter()

@etl_router.post('/erp/test',tags=["TEST"], response_model=ApiResponseSchema)
def dwTEST(request_body: EtlBasic):

    # URL de la API REST
    url = 'https://cloud.grupotsiperu.com.pe:8000/erp/test'

    # Realizar la solicitud POST
    response = requests.post(url, json= jsonable_encoder(request_body), verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Devolver los datos como respuesta en formato JSON
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise HTTPException(status_code=response.status_code, detail=response.text)

@etl_router.post('/erp/dataset/dw-cventa-dataset',tags=["CVENTA"], response_model=ApiResponseSchema)
def dwCVENTADataset(request_body: EtlBasic):

    # URL de la API REST
    # url = 'https://cloud.grupotsiperu.com.pe:8000/erp/dataset/dw-cventa-dataset'

    # # Realizar la solicitud POST
    # response = requests.post(url, json=jsonable_encoder(request_body), verify=False)
    
    # # Comprobar el estado de la respuesta
    # if response.status_code == 200:
    #     # Devolver los datos como respuesta en formato JSON
    #     return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    # else:
    #     # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
    #     raise HTTPException(status_code=response.status_code, detail=response.text)
    
    # Simular un retraso de 2 segundos
    time.sleep(2)

    # Crear una respuesta JSON
    response_data = {
        "status": 1,
        "message": "Proceso finalizado, se actualizaron un total de 41553 registros!"
    }

    return JSONResponse(status_code=status.HTTP_200_OK, content=response_data.json())

@etl_router.post('/erp/dataset/dw-cxc-dataset',tags=["CXC"], response_model=ApiResponseSchema)
def dwCXCDataset(request_body: EtlBasic):

    # # URL de la API REST
    # url = 'https://cloud.grupotsiperu.com.pe:8000/erp/dataset/dw-cxc-dataset'

    # # Realizar la solicitud POST
    # response = requests.post(url, json=jsonable_encoder(request_body), verify=False)

    # # Comprobar el estado de la respuesta
    # if response.status_code == 200:
    #     # Devolver los datos como respuesta en formato JSON
    #     return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    # else:
    #     # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
    #     raise HTTPException(status_code=response.status_code, detail=response.text)

    # Simular un retraso de 2 segundos
    time.sleep(2)

    # Crear una respuesta JSON
    response_data = {
        "status": 1,
        "message": "Proceso finalizado, se actualizaron un total de 653 registros!"
    }

    return JSONResponse(status_code=status.HTTP_200_OK, content=response_data.json())

@etl_router.post('/erp/dataset/dw-cventa-minidataset', tags=["CVENTA"], response_model=ApiResponseSchema)
def dwCVENTAMiniDataset(request_body: EtlBasic):

    # URL de la API REST
    url = 'https://cloud.grupotsiperu.com.pe:8000/erp/dataset/dw-cventa-minidataset'

    # Realizar la solicitud POST
    response = requests.post(url, json=jsonable_encoder(request_body), verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Devolver los datos como respuesta en formato JSON
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise HTTPException(status_code=response.status_code, detail=response.text)

@etl_router.post('/erp/dataset/dw-proyeccion', tags=["PROYECCION"], response_model=ApiResponseSchema)
def dwPROYECCIONDataset(request_body: EtlBasic):

    # URL de la API REST
    url = 'https://cloud.grupotsiperu.com.pe:8000/erp/dataset/dw-proyeccion'

    # Realizar la solicitud POST
    response = requests.post(url, json=jsonable_encoder(request_body), verify=False)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Devolver los datos como respuesta en formato JSON
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())
    else:
        # Devolver un mensaje de error en caso de que la solicitud no sea exitosa
        raise HTTPException(status_code=response.status_code, detail=response.text)