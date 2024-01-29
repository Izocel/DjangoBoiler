import logging

from projects.loggers.appLogger import API_LOGGER, APP_LOGGER, TOOLS_LOGGER


class Tools:
	@staticmethod
	def help():
		APP_LOGGER.debug("debug message", extra={"x": "hello"})
		APP_LOGGER.info("info message")
		APP_LOGGER.warning("warning message")
		APP_LOGGER.error("error message")
		APP_LOGGER.critical("critical message")

		API_LOGGER.debug("debug message", extra={"x": "hello"})
		API_LOGGER.info("info message")
		API_LOGGER.warning("warning message")
		API_LOGGER.error("error message")
		API_LOGGER.critical("critical message")
		
		TOOLS_LOGGER.debug("debug message", extra={"x": "hello"})
		TOOLS_LOGGER.info("info message")
		TOOLS_LOGGER.warning("warning message")
		TOOLS_LOGGER.error("error message")
		TOOLS_LOGGER.critical("critical message")
		try:
			1 / 0
		except ZeroDivisionError:
			TOOLS_LOGGER.exception("exception message")