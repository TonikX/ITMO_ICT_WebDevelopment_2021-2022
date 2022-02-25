include .env
export

init:
	mkdir data && cp configs/settings_production_example.py check_splitter/settings_local.py && cp .env.sample .env && docker volume create --name check_splitter_db -d local

dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

run:
	docker-compose up -d --build

stop:
	docker-compose stop

logs:
	docker-compose logs --tail=1000 --follow

bash:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 bash

psql:
	docker exec -it ${COMPOSE_PROJECT_NAME}_db_1 psql --username ${COMPOSE_PROJECT_NAME}

shell:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 python manage.py shell_plus

populate:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 bash -c "python manage.py populate"

test:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 bash -c "python manage.py test"
