Comparte Ride
=============

Group-bounded, invite-only, carpooling platform

export COMPOSE_FILE=local.yml
	
sudo docker-compose -f local.yml ps
sudo docker rm -f django-cride-xxxx
sudo docker-compose -f local.yml run --rm --service-ports django python manage.py runserver
useradmin: jesus.herrera@copamex.com.mx


### remove a volume 6s
sudo docker-compose -f local.yml down
sudo docker volume ls
sudo docker volume rm nombre_de_volumen

### debugger
import pdb; pdb.set_trace()

