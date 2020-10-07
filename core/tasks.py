from celery import shared_task
from celery.utils.log import get_task_logger
import random

logger = get_task_logger(__name__)


@shared_task
def every_10_sec():
    logger.info("Run every 10sec methods")
    result = random.randint(0, 100) + random.randint(0, 100)
    logger.info("result: %s" % result)
    return result

@shared_task
def every_30_sec():
    logger.info("Run every 30sec methods")
    result = random.randint(0, 100) + random.randint(0, 100)
    logger.info("result: %s" % result)
    return result
