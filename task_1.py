from re import sub


def to_camel_case(text):
    s = sub(r"(_|-)+", " ", text).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


class SingletonMeta(type):
    _instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def count_bits(n):
    b = bin(n).count('1')
    return b


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
