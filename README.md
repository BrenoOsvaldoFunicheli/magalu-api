# magalu API

## Backend Challenge to provide the API implementation

A complete implementation of RESTful API to store and consume some structures that it contains, which were created using django 3 and django rest_framework.

## Sections

* :scroll: [Patterns](#scroll-patterns) (optional)
* :blue_book: [Requirements and Model](#blue_book-requirements-and-model)
* :postbox: [Testing](#postbox-testing)
* :wrench: [Building App](#wrench-building-app)
* :key: [Authentication](#key-authentication)
* :ticket: [API Consuming](#ticket-api-consuming)

## :scroll: Patterns

In order to create the real stage API to consuming I follow some best pratice and concepts of RESTful APIs must has, beside this, I provide the detailed documentation about API with the postman to test endpoints.

### Implemented concepts

* Versioning: All endpoints contains as prefix /api/v1/ that show the version api is first. So when I change some detail or implementation of API I Don't broken any implementation on my API in other application.

* Pagination: As many people can consuming the endpoints I need provide some throughput data. to first version we apply the limit with 5 registries.

* Authentication: I make the API visualization with the JWT tokens to Authentication on each endpoints

## :blue_book: Requirements

The system consists of a creator of send requests API, where you can register using email and password, and schedule some requests to send after.

### Requirements

* Authentication: The user registry himself with the password and email and can be get the token to access any endpoint to create and delete his registry by request.

* User tracked: In order to provide some security and isolation of registry all user only have access to own registry with exception of the dad tables, such as tecnologies and jobs.

* Send Requests Endpoint
    - Create: create new request to send
    - List: return all values
    - Retrive: return the specific
    - Update: alter status
    - Delete: delete the registry


## :postbox: Testing

Test automation is the use of software to control the execution of the software test, the comparison of the expected results with the actual results, the configuration of the test pre-conditions and other control and test report functions.
In this repository I provide some task to show the knowledge with tests.

## :wrench: Building App

There are two way to build and run this application, first is running with isolate app, second is with docker that separates the context and allows running withou previous dependecies.  

### Normal build

1. Get repository
2. Make the virtualenv
3. Run o virtualenv
4. Install all dependecies
5. Run test
6. Run migrations
7. Run app

```console

    git clone https://github.com/BrenoOsvaldoFunicheli/magalu-api
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt
    python manage.py test
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8002

```

### Docker Build

This API was construct with the docker implementation, so you can run without others dependecies and scale after make your implementations, so you need make docker and docker compose in your machine.

#### Docker installation

To install docker follow the instructions in the links below depending on your operating system:

* CentOS: https://docs.docker.com/install/linux/docker-ce/centos/
* Debian: https://docs.docker.com/install/linux/docker-ce/debian/
* Fedora: https://docs.docker.com/install/linux/docker-ce/fedora/
* Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* MacOS: https://docs.docker.com/docker-for-mac/install/
* Windows: https://docs.docker.com/docker-for-windows/install/

#### Step by Step to Set Up

For API build you need some simple steps, download the this repository with the follow command:

``` linux

git clone https://github.com/BrenoOsvaldoFunicheli/magalu-api

```

before the next step you need create the docker-volume to store the database data.

``` linux

docker volume create magalu

```

Next, you need setting the app and database containers with the follow command on the folder downloaded, that make(download all dependencies of the project), building(when you don't have container in your machine it downloaded it) and setting containers with docker compose.

``` linux

docker-compose build

docker-compose up

```

After this you need create database on container, because django can't create automatic, the database container is running the postgres. so you need create the database with the name magalu.

* Docker attach

``` linux

docker exec -it [container-name] /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"

```

* Postgres DDL

``` sql

CREATE DATABASE magalu;

```

Next, you can't press CTRL+C to exit database and set it up again with the docker-compose up, with this you'll have the API running, but you need migrate database changes with follow command:

* migrations

``` linux

docker exec -it [container-name] /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"

python manage.py makemigrations

python manage.py migrate

```

Finally, you can use the API !!!

## :key: Authentication

As the API was implemented with JWT tokens all access on the endpoints are do with the jwt tokens, so you need apply the request and set in the authorization.

### Token duration

So when you access token through the url [uri]/api/v1/[resource] you can get two values on the payload response, first is the access token, with it, you can access the endpoint for 5 minutes, after you need used the refresh endpoint that gives the token to access for 24 hours.  

## :ticket: API Consuming

The API consuming were detailed on the postman collection, that implements all steps to consuming and explain some steps to use. The ordering of steps need to be follow, because you need authentication before consuming. The collection link is 

### Example of the code to create super user

```linux

python manage.py createsuperuser --username django --email django@django.com
# so, create user to you

```
