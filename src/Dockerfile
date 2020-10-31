FROM python:3

WORKDIR /usr/src/app

COPY . ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# COPY . /usr/src/app

CMD [ "python", "/usr/src/app/test.py" ]
