import json
import random
import string

import numpy as np


def generate(
    length: int = 8, include_letters: bool = False, include_symbols: bool = False
):
    numbers = string.digits
    letters = string.ascii_letters
    symbols = string.punctuation
    chars = numbers
    if include_letters:
        chars += letters
    if include_symbols:
        chars += symbols
    random_string = "".join(random.choice(chars) for _ in range(length))
    return random_string


def read_json(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"文件{file_path}没找到")


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.dtypes):
            return str(obj)
        return super().default(obj)


if __name__ == "__main__":
    print(generate(3))
