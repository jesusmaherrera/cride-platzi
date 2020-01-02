Comparte Ride
=============

Group-bounded, invite-only, carpooling platform

export COMPOSE_FILE=local.yml
sudo docker-compose -f lcoal.yml up
sudo docker-compose -f lcoal.yml ps
sudo docker rm -f django-cride-xxxx
sudo docker-compose -f lcoal.yml run --rm --service-ports django python manage.py runserver

