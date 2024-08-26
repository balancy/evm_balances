all: up

lint:
	ruff check backend
	black --check backend

up:
	docker-compose up -d --build