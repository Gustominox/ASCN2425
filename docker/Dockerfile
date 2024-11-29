# 22.04 
FROM ubuntu:22.04

# frontend não-interativo evita prompts durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# dependencias
RUN apt-get update && apt-get install -y \
    python3-pip \  
    libpq-dev \  
    build-essential \  
    python3-dev \  
    curl \  
    && apt-get clean  

# diretoria
WORKDIR /app

# copiar requirements
COPY codebase/moonshot/requirements.txt /app/

# instalar requirements.txt
RUN pip install --no-cache-dir -r requirements.txt  

# copiar moonshot 
COPY codebase/moonshot /app/

# migrações e seed da base de dados
RUN python3 /app/manage.py migrate && \
    python3 /app/seed.py

# Expor a porta 8000
EXPOSE 8000

# executar o servidor diretamente
CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:8000"]
