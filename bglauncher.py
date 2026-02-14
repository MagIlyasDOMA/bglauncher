import sys, subprocess
from datetime import datetime
from pathlike_typing import PathLike
from typing import Optional, Iterable

__version__ = '1.0.0'


def log(*values, sep: str = ' ', end: str = '\n', first_file=sys.stdout) -> None:
    values = [f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"] + list(values)
    with open('bglauncher.log', 'a') as file:
        print(*values, sep=sep, end=end, file=first_file)
        print(*values, sep=sep, end=end, file=file)


def run_bg(program_path: PathLike, args: Optional[Iterable] = None):
    """Запускает программу в фоновом режиме"""
    if args is None: args = []

    try:
        if sys.platform == "win32":
            process = subprocess.Popen(
                [program_path] + list(args),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        else:
            process = subprocess.Popen(
                [program_path] + args,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                start_new_session=True
            )
        log(f"The program is running with PID: {process.pid}")
        return process
    except subprocess.CalledProcessError as e:
        log(f"The program failed with exit code: {e.returncode}")
    except Exception as e:
        log(f"Startup error: {e}")
        return None


def main():
    if len(sys.argv) == 1:
        log("The path to the program is not specified.", first_file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv) == 2:
        process = run_bg(sys.argv[1])
    else:
        process = run_bg(sys.argv[1], sys.argv[2:])
    log("Process exit code: ", process.returncode)


if __name__ == '__main__': main()
