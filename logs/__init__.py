import logging

# create logger
logger = logging.getLogger("ferramenta-TCC")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#define file to save loggings
# logging.basicConfig(filename="loggings.txt",format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def log(log_type: str, msg: str) -> None:
    if log_type == "i":
        return logger.info(msg)
    elif log_type == "e":
        return logger.error(msg, exc_info=True)
