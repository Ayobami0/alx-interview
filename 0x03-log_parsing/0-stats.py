#!/usr/bin/python3

import signal
import sys
import re

_store = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
_total_size = 0
_reg = re.compile(
    r'^(\d|.*)\s-\s\[(.*)\]\s"GET\s\/'
    + r'projects\/260\sHTTP\/1.1"\s(\d{3})\s(\d{1,4})'
)
_counter = 0


def _print_stats():
    print(
        "File size: {}".format(_total_size),
        "\n".join(["{}: {}".format(k, v) for k, v in _store.items()]),
        sep="\n",
        end="\n",
    )


def _handler(signum, frame):
    _print_stats()


signal.signal(signal.SIGINT, _handler)

for line in sys.stdin:
    if _counter == 10:
        _print_stats()
        _counter = 0
        continue

    matched = _reg.search(line.strip())

    if not matched:
        continue

    try:
        file_size = int(matched.group(4))
        st_code = int(matched.group(3))
    except Exception:
        continue

    if _store.get(st_code, None) is None:
        continue

    _store[st_code] += 1
    _total_size += file_size
    _counter += 1
