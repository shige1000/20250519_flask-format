FROM python:3.12-slim

WORKDIR /src

RUN apt-get update \
    && apt-get install -y --no-install-recommends\
        # Mysql利用用
        libmariadb-dev \
        libmariadb-dev-compat \
        # Pythonパッケージ利用用
        gcc \
        pkg-config \
        # gunicorn停止用
        procps \
    # Docker内の軽量化
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY src /src

WORKDIR /src/project
CMD ["python", "wsgi.py"]
