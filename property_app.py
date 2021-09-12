from fastapi import FastAPI
from services.get_properties_microservice import get_properties

app = FastAPI()


@app.get("/properties")
def properties():
    return get_properties("", "all_properties")


@app.get("/properties_filtered/")
def properties_by_city(city: str, year: int, status: str):
    return get_properties((city, year, status), "properties_filtered")


@app.get("/properties_by_price/")
def properties_by_price(lower_limit: float, upper_limit: float):
    return get_properties((lower_limit, upper_limit), "filtered_by_price")
