from celery import Celery

app = Celery("doeapi.tasks", broker="redis://localhost:6379/0")

app.autodiscover_tasks(["doeapi.tasks"])
app.config_from_object("doeapi.celeryconfig")
