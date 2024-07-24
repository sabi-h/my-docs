#### Pull lightweight postgres images for local testing
	docker pull postgres:alpine


#### Run docker image
	docker run --name omega-postgres -e POSTGRES_PASSWORD=iiposju -p 5432:5432 -d postgres:alpine


#### Bash into container
	docker exec -it omega-postgres bash
