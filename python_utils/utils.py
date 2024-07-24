import time
from datetime import datetime, timedelta
from functools import wraps

import functools
import logging

LOGGER_NAME = "my-awesome-logger"


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    logs_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(logs_format)

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


logger = get_logger(LOGGER_NAME)


def log(func):
    @functools.wraps(func)  # Preserves function meta-data when it is decorated
    def wrapper(*args, **kwargs):
        function_path = f"{func.__module__}.{func.__name__}"
        logger.info(f"RUNNING: {function_path}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"FINISHED: {function_path}")
            return result
        except Exception as e:
            logger.exception(f"error: Function {function_path} raised an exception: {e}")
            raise

    return wrapper


def calc_no_of_pages(items: int, per_page: int = 100) -> int:
    """Takes number of items and calculates number of pages needed based on items per page."""
    return (items // per_page) + bool(items % per_page)


def add_one_second_to_datetime(date_string: str) -> str:
    return (datetime.fromisoformat(date_string) + timedelta(seconds=1)).isoformat()


def log_and_handle_exception(_func=None, *, logger=logger):
    def decorator_exception(func):
        @wraps(func)
        def exception_wrapper(*args, **kwargs):
            function_path = f"{func.__module__}.{func.__name__}"
            logger.info(f"RUNNING: {function_path}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"SUCCESS: {function_path}")
                return result
            except Exception:
                logger.exception(f"Error occured in function: {func.__name__}")
                logger.info(f"FAILED: {function_path}")

        return exception_wrapper

    if _func is None:
        return decorator_exception
    else:
        return decorator_exception(_func)


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logger.info(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper
