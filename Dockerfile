FROM python

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    	binutils libproj-dev gdal-bin && \
    apt-get clean

ENV APP_DIR /usr/src/app

RUN mkdir -p $APP_DIR

COPY requirements.txt /usr/src/app/

RUN pip install -r $APP_DIR/requirements.txt

WORKDIR /usr/src/app

EXPOSE 8000

CMD ["python", "geodjango/manage.py", "runserver", "0.0.0.0:8000"]
