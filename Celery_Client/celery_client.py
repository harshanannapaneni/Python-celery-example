from cel_main import TaskQueue, write_log

TaskQueue.delay("First task for celery")
write_log.delay("The logs are here.")