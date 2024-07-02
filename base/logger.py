import logging
import logging.config
import os

import yaml


class Logger(object):
    def __init__(
        self, name="Default", config_path="logging_config.yaml"
    ) -> None:
        self._config_path = config_path
        self.set_conf()
        self.__logger = logging.getLogger(name)

    def set_conf(self):
        with open(self._config_path, "r", encoding="utf-8") as f:
            config = yaml.load(f, yaml.SafeLoader)

        logging.config.dictConfig(config)

    @property
    def conf_path(self):
        return f"{os.getcwd()}/{self._config_path}"

    @conf_path.setter
    def conf_path(self, new_path):
        if not os.path.exists(new_path):
            self.__logger.error(f"Config file [{new_path}] is not exist!")
            raise FileNotFoundError

        self._config_path = new_path

    def info(self, msg: str):
        self.__logger.info(msg)

    def debug(self, msg: str):
        self.__logger.debug(msg)

    def warn(self, msg: str):
        self.__logger.warning(msg)

    def error(self, msg: str):
        self.__logger.error(msg)
