#le indico la version del contenedor
FROM python:3.9

#creo una carpeta dentro de ese contenedor
WORKDIR /app

#copia el archivo de dependencias a el contenedor
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"