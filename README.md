### RabbitMQ

#### Command to spin up a container of rabbitmq:

docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management

### Install celery:

uv add celery or pip install celery

### Command to start the celery worker

#### For linux:

celery -A cel_main worker --loglevel=INFO

#### For windows:

include: --pool=solo
