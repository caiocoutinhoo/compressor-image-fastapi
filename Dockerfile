# Use uma imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir

# Copia o código da aplicação para o container
COPY . .

# Expõe a porta que a aplicação usará
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
