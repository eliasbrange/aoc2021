def read_file(filename: str):
    with open(filename) as f:
        for line in f:
            if line.strip():
                yield line.strip()
