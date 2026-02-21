from cel_main import TaskQueue, write_log, email_send
from celery import group

TaskQueue.delay("First task for celery")
write_log.delay("The logs are here.")


# Create group of tasks (parallel execution)
dummy_emails = [
    "alex.johnson01@example.com",
    "emma.williams02@example.com",
    "liam.brown03@example.com",
    "olivia.jones04@example.com",
    "noah.garcia05@example.com",
    "ava.miller06@example.com",
    "william.davis07@example.com",
    "sophia.rodriguez08@example.com",
    "james.martinez09@example.com",
    "isabella.hernandez10@example.com",
    "benjamin.lopez11@example.com",
    "mia.gonzalez12@example.com",
    "lucas.wilson13@example.com",
    "amelia.anderson14@example.com",
    "henry.thomas15@example.com",
    "harper.taylor16@example.com",
    "alexander.moore17@example.com",
    "evelyn.jackson18@example.com",
    "michael.martin19@example.com",
    "abigail.lee20@example.com",
    "daniel.perez21@example.com",
    "ella.thompson22@example.com",
    "matthew.white23@example.com",
    "avery.harris24@example.com",
    "jack.sanchez25@example.com",
    "scarlett.clark26@example.com",
    "sebastian.ramirez27@example.com",
    "grace.lewis28@example.com",
    "david.robinson29@example.com",
    "chloe.walker30@example.com",
    "joseph.young31@example.com",
    "victoria.allen32@example.com",
    "samuel.king33@example.com",
    "riley.wright34@example.com",
    "andrew.scott35@example.com",
    "lily.torres36@example.com",
    "gabriel.nguyen37@example.com",
    "zoey.hill38@example.com",
    "carter.flores39@example.com",
    "natalie.green40@example.com",
]

job = group(email_send.s(email) for email in dummy_emails)

job.apply_async()

print("All email tasks queued successfully!")