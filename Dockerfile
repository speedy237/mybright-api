# Utiliser une image officielle de Python
FROM python:3.9-slim-buster

# Définir le répertoire de travail
WORKDIR /mybright

# Copier les fichiers de l'application
COPY requirements.txt .
COPY main.py .
COPY base.py .
COPY model.py .
COPY brightM_database.db .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Lancer l'application FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
