# Use a imagem oficial do Python como base
FROM python:3.7-slim

# Defina o diretório de trabalho principal
WORKDIR /app

# Copie o arquivo de configuração para o diretório de trabalho principal
COPY config_example.yml /app/

# Copie o diretório src para o contêiner
COPY src/ /app/src

# Copie o arquivo de dependências para o diretório de trabalho principal
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Defina a variável de ambiente necessária para o Flask
ENV KLEIN_CONFIG=/app/config_example.yml

# Defina o diretório de trabalho como /app/src para a execução do Gunicorn
WORKDIR /app/src

# Exponha a porta 8080
EXPOSE 8080

# Comando para rodar o aplicativo Flask usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
