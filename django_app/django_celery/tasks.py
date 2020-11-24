from .celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(bind=True)
def debug_task(self):
    logger.debug(f"Request: {self.request!r}")
