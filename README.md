# PyDHT11 API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## Environment

- Python 3.11.+ (3.9.+ or 3.10.+ should work too)
- Raspberry Pi 3B+ (or any other Raspberry Pi with GPIO pins)
- DHT11 sensor

## Setup steps (Raspberry Pi)


```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```