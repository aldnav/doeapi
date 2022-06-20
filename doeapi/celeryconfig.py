from celery.beat import crontab

broker_url = "redis://localhost:6379/0"

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
enable_utc = True

beat_schedule = {
    "fetch-retail-oil-every-minute": {
        "task": "doeapi.tasks.fetch_retail_oil.hello",
        "schedule": crontab(minute="*"),
    }
}
