all: build run

build:
	docker build -t vulnerable-flask .

run:
	docker inspect vulnerable-flask >/dev/null 2>&1 && docker rm -f vulnerable-flask || true
	docker run --rm --name vulnerable-flask -p 5000:80 -t vulnerable-flask
