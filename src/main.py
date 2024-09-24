from fastapi import FastAPI, HTTPException
import httpx
import requests
import app.utils.constants as constants

app = FastAPI()

@app.get("/send-request/")
def send_request():
    # Post
    # POST https://app.scrapingbee.com/api/v1
    try:
        response = requests.post(
            url="https://app.scrapingbee.com/api/v1",
            params={
                "url": "https://httpbin.org/anything",
                "api_key": constants.SCRAPINGBEE_API_KEY,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            data={
                "KEY_1": "VALUE_1",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

@app.get("/scrape-title/")
async def scrape_title(url: str):
    params = {
        'api_key': SCRAPINGBEE_API_KEY,
        'url': url,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(SCRAPINGBEE_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {"title": data.get("title", "Título no encontrado")}
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al hacer scraping")

async def login_user(credentials):
    return {"message": "Usuario autenticado", "credentials": credentials}

async def review_properties():
    return {"properties": ["propiedad1", "propiedad2"]}

async def import_properties(data):
    return {"message": "Propiedades importadas", "data": data}

async def export_active_reservations():
    return {"reservations": ["reserva1", "reserva2"]}

async def reject_reservation(reservation_id):
    return {"message": f"Reserva {reservation_id} rechazada"}

async def accept_reservation(reservation_id):
    return {"message": f"Reserva {reservation_id} aceptada"}

async def export_tenant_data(tenant_id):
    return {"tenant_data": {"id": tenant_id, "name": "Inquilino Ejemplo"}}

@app.post("/login")
async def login(credentials: dict):
    return await login_user(credentials)

@app.get("/properties")
async def get_properties():
    return await review_properties()

@app.post("/import_properties")
async def import_props(data: dict):
    return await import_properties(data)

@app.get("/active_reservations")
async def active_reservations():
    return await export_active_reservations()

@app.post("/reject_reservation/{reservation_id}")
async def reject_reservation_endpoint(reservation_id: int):
    return await reject_reservation(reservation_id)

@app.post("/accept_reservation/{reservation_id}")
async def accept_reservation_endpoint(reservation_id: int):
    return await accept_reservation(reservation_id)

@app.get("/tenant_data/{tenant_id}")
async def tenant_data(tenant_id: int):
    return await export_tenant_data(tenant_id)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
