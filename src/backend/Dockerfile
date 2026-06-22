FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Commande pour lancer le backend (exemple avec Uvicorn pour FastAPI/Django)
CMD ["uvicorn", "scoring:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]