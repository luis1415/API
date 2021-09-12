import grpc
import property_pb2
import property_pb2_grpc
from fastapi import FastAPI
from services.get_properties_microservice import get_properties

tags_metadata = [{"name": "properties"}, {"name": "grpc consulta"}]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="Consultar Propiedades",
    description="API",
    version="0.0.1",
)


def grpc_request(property_id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = property_pb2_grpc.PropertyStub(channel)
        response = stub.Properties(
            property_pb2.PropertyRequest(property_id=property_id))
    return response


@app.get("/property/{id}", tags=["grpc consulta"])
def properties(id: int):
    grpc_response = grpc_request(id)
    return {
        "adress": grpc_response.address,
        "city": grpc_response.city,
        "price": grpc_response.price,
        "description": grpc_response.description
    }


@app.get("/properties", tags=["properties"])
def properties():
    return get_properties("all_properties")


@app.get("/properties_filtered/", tags=["properties"])
def properties_by_city(city: str, year: int, status: str):
    return get_properties("properties_filtered", (city, year, status))


@app.get("/properties_by_price/", tags=["properties"])
def properties_by_price(lower_limit: float, upper_limit: float):
    return get_properties("filtered_by_price", (lower_limit, upper_limit))
