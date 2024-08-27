all: dev

lint:
	ruff check backend
	black --check backend

dev:
	docker-compose up -d --build

prod:
	docker-compose -f docker-compose.yml up -d --build