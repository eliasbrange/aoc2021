from typing import Callable, Iterator, Any


def read_file(
    filename: str,
    func: Callable[[str], Any] = None,
) -> Iterator[Any]:
    with open(filename) as f:
        for line in f:
            if func:
                yield func(line.strip())
            else:
                yield line.strip()
