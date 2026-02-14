from sys import stderr
from constants import LOG_FILE

try:
    LOG_FILE.write_text('')
    print(f"Log file {LOG_FILE} cleaned successfully")
except Exception as error:
    print(error.__class__.__name__, str(error), sep=': ', file=stderr)
