import time
from services.common.logger import get_logger

log = get_logger("worker")

def run_with_retry(fn, retries=5):
    for i in range(retries):
        try:
            return fn()
        except Exception as e:
            log.error(f"Error: {e}")
            time.sleep(2 ** i)
    raise RuntimeError("Max retries exceeded")
