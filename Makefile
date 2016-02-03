build:
	docker build -t geodjango .
run:
	docker run --rm --privileged=true -p 80:8000 \
	-v `pwd`:/usr/src/app --link postgis:db --name geodjango \
	geodjango
runbash:
	docker run --rm -ti --privileged=true -p 80:8000 \
	-v `pwd`:/usr/src/app --link postgis:db --name geodjango \
	geodjango /bin/bash
bash:
	docker exec -ti geodjango /bin/bash
makemigrations:
	docker run --rm -ti --privileged=true \
	    -v `pwd`:/usr/src/app \
	    geodjango geodjango/manage.py makemigrations geo
migrate:
	docker run --rm --privileged=true \
	    -v `pwd`:/usr/src/app \
	    geodjango geodjango/manage.py migrate
createsuperuser:
	docker exec -ti geodjango geodjango/manage.py createsuperuser
