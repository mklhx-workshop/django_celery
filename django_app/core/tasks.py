from celery import app
from celery.utils.log import get_task_logger
import random

logger = get_task_logger(__name__)

@app.shared_task
def every_10_sec():
    logger.info("Run every 10sec methods")
    result = random.randint(0, 100) + random.randint(0, 100)
    logger.info("result: %s" % result)
    return result


@app.shared_task
def every_30_sec():
    logger.info("Run every 30sec methods")
    result = random.randint(100, 200) + random.randint(200, 300)
    logger.info("result: %s" % result)
    return result


@app.shared_task
def every_60_sec():
    logger.info("Run every 60sec methods")
    result = random.randint(300, 400) + random.randint(400, 500)
    logger.info("result: %s" % result)
    return result
