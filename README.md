# PyDHT11 API

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

[![micheltlutz github](https://img.shields.io/badge/GitHub-micheltlutz-181717.svg?style=flat&logo=github)](https://github.com/micheltlutz)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)


## Environment

- Python 3.11.+ (3.9.+ or 3.10.+ should work too)
- Raspberry Pi 2B+ (or any other Raspberry Pi with GPIO pins)
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
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Access

> Change localhost to your Raspberry Pi IP address to access from another device

- [http://localhost:8000/docs](http://localhost:8000/docs)



![Routes Available](readme_files/api.png "Routes Available")
