# 22.04 
FROM python:3.11.5-slim

# Frontend não-interativo evita prompts durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Dependências
RUN apt-get update && apt-get install -y \
    python3-pip \  
    libpq-dev \  
    build-essential \  
    python3-dev \  
    curl \
    postgresql-client \  
    && apt-get clean  

# Diretório de trabalho
WORKDIR /app

# Copiar requirements
COPY codebase/moonshot/requirements.txt /app/

# Instalar requirements.txt
RUN pip install --no-cache-dir -r requirements.txt  

# Copiar moonshot 
COPY codebase/moonshot /app/

# Expor a porta 8000
EXPOSE 8000

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Executar o servidor e migrações no startup
CMD ["sh", "-c", "python3 /app/manage.py migrate && python3 /app/seed.py && python3 /app/manage.py runserver 0.0.0.0:8000"]
