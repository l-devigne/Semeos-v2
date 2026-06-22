COMPOSE = docker compose -f docker-compose.yml

.PHONY: all build up down exec exec-ollama logs clean fclean

all: up

# build:
# 	$(COMPOSE) build

up: build
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down

exec-backend:
	$(COMPOSE) exec -it backend bash

exec-frontend:
	$(COMPOSE) exec -it frontend bash

exec-database:
	$(COMPOSE) exec -it database bash

logs:
	$(COMPOSE) logs -f

clean: down

fclean: down
	$(COMPOSE) down -v --rmi local
