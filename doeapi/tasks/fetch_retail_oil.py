from doeapi import app


@app.task
def hello():
    return "Hello"
