import Adafruit_DHT
import logging
import uvicorn

from decouple import config
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any origin. Don't do this in production!
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],
)

# Definir o tipo de sensor
DHT_SENSOR = Adafruit_DHT.DHT11

# Definir o pino ao qual o sensor está conectado
DHT_PIN = 4  # Considerando que o sensor esteja conectado ao GPIO4


@app.get("/")
def redirect_to_docs():
    response = RedirectResponse(url='/docs')
    return response


@app.get("/health-check")
def health_check():
    return JSONResponse(
        content={"status": "ok"},
        status_code=status.HTTP_200_OK
    )


@app.get("/version")
def health_check():
    return JSONResponse(
        content={"version": config("VERSION")},
        status_code=status.HTTP_200_OK
    )


@app.get("/dht11", response_model=dict)
def get_dht11_data():
    """
    Busca os dados de umidade e temperatura do sensor DHT11
    """
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            return {
                "temperature": f"{temperature:.2f}C",
                "humidity": f"{humidity:.2f}%"
            }
        else:
            logging.error("Falha ao receber a leitura do sensor DHT11.")
            raise HTTPException(status_code=500, detail="Erro na leitura do sensor DHT11.")
    except Exception as e:
        logging.error(f"Erro ao ler o sensor DHT11: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor.")



#uvicorn.run(app, host="0.0.0.0", port=8000)