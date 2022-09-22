FROM python:3.8.13

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
COPY ./app /code/app

WORKDIR /code/app
# 80 portum dolu
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8188"]
