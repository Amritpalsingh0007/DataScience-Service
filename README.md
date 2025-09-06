# DataScience-Service

A modular **FastAPI-based service** for running data science workflows and experiments.  
This project is structured to support scalable development with separate modules, packaging support, and Docker deployment.

---

## 🚀 Features
- Built with **FastAPI** for high-performance APIs.
- Packaged as a Python distribution (`.tar.gz`) for easy installation.
- Dockerized for consistent deployments.
- Ready to integrate with ML/Data pipelines.

---

## 📂 Project Structure
ds-service/
├── utils/
├── models/
├── service/
├── main.py

---

## ⚡ Getting Started

### Prerequisites
- Need Google gemini api key
- Python 3.9+ (Recommended: Python 3.13)
- [Uvicorn](https://www.uvicorn.org/) ASGI server
- [FastAPI](https://fastapi.tiangolo.com/)

### Installation (Development)

```bash
git clone https://github.com/Amritpalsingh0007/DataScience-Service.git
cd DataScience-Service

# Install dependencies
pip install -r requirements.txt
````

### Run Locally

```bash
python main.py
```

or using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🐳 Run with Docker

### Build Image

```bash
docker build -t ds-service -f Dockerfile .
```

### Run Docker Compose
Note: Other service in the `docker-compose.yaml` file are all in my github.
```bash
docker compose up
```

---

## 🔧 API Endpoints

Once running, open the interactive API docs:

* Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---
