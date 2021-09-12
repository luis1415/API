from fastapi import FastAPI
from services.get_properties_microservice import get_properties

tags_metadata = [{"name": "properties"}]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="Consultar Propiedades",
    description="API",
    version="0.0.1",
)


@app.get("/properties", tags=["properties"])
def properties():
    return get_properties("all_properties")


@app.get("/properties_filtered/", tags=["properties"])
def properties_by_city(city: str, year: int, status: str):
    return get_properties("properties_filtered", (city, year, status))


@app.get("/properties_by_price/", tags=["properties"])
def properties_by_price(lower_limit: float, upper_limit: float):
    return get_properties("filtered_by_price", (lower_limit, upper_limit))
