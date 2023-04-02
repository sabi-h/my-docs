#### Pull lightweight postgres images for local testing
	docker pull postgres:alpine


#### Run docker image
	docker run --name omega-postgres -e POSTGRES_PASSWORD=admin -d postgres:alpine


#### Bash into container
	docker exec -it omega-postgres bash
