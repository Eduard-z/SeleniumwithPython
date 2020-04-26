import logging

logging.basicConfig(filename=r"C:\Users\zakharove\PycharmProjects\SeleniumwithPython\log.txt",
                    level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s:',
                    datefmt='%m/%d/%Y %I: %M: %S %p')

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
