FROM python:3.10

COPY . /DnD_Monsters/deployment
# Set the working directory
WORKDIR /DnD_Monsters/deployment

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


CMD ["gunicorn", "app:server", "-b", "0.0.0.0:80", "--timeout", "75", "--log-level", "error"]


EXPOSE 80