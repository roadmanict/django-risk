build:
	docker build -t geodjango .
run:
	docker run --rm geodjango
bash:
	docker run --rm -ti geodjango /bin/bash
makemigrations:
	docker run --rm -ti \
	    -v `pwd`:/usr/src/app:z \
	    geodjango /usr/src/app/geodjango/manage.py makemigrations geo
