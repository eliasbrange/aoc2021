from typing import Callable


def read_file(filename: str, func: Callable[[str], None] = None):
    with open(filename) as f:
        for line in f:
            if func:
                yield func(line.strip())
            else:
                yield line.strip()
