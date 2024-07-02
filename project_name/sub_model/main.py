from base.logger import Logger

logger = Logger(__name__)


class C11(object):
    def __init__(self) -> None:
        logger.debug("Creating instance of C11")
