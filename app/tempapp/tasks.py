from celery import shared_task
from celery.utils.log import get_task_logger

log = get_task_logger(__name__)


@shared_task(bind=True)
def do_nothing(self, pk):
    log.info(f'Doing nothing with pk {pk}]')
