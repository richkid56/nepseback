from fastapi import FastAPI
from scraper import get_today_prices

app = FastAPI()

@app.get("/prices/today")
def today_prices():
    return get_today_prices()