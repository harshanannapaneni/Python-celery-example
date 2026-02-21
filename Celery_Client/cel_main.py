from celery import Celery
import time

# app = Celery("cel_main", broker="pyamqp://")
app = Celery("cel_main", broker="pyamqp://localhost//")


@app.task
def TaskQueue(message):
    time.sleep(10)
    print("TaskQueue: {0}".format(message))


@app.task
def write_log(logs):
    print("Writing logs: {0}".format(logs))