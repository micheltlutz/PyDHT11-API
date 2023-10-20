import Adafruit_DHT
import time
import logging

# Configurações do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Definir o tipo de sensor
DHT_SENSOR = Adafruit_DHT.DHT11

# Definir o pino ao qual o sensor está conectado
DHT_PIN = 4  # Considerando que o sensor esteja conectado ao GPIO4

def read_dht11_data():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            logging.info(f"Temperatura={temperature:.2f}C  Umidade={humidity:.2f}%")
        else:
            logging.error("Falha ao receber a leitura do sensor DHT11. Tentando novamente...")
    except Exception as e:
        logging.error(f"Erro ao ler o sensor DHT11: {e}")

if __name__ == "__main__":
    while True:
        read_dht11_data()
        time.sleep(2)  # Aguarde 2 segundos antes da próxima leitura
