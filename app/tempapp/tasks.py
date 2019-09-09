import logging

logger = logging.getLogger(__name__)


def do_nothing(pk):
    logger.info(f'Doing nothing with pk {pk}]')
