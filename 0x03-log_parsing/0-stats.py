#!/usr/bin/python3
"""Log parsing"""


import sys

if __name__ == "__main__":
    fileSize = 0
    count = 0

    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {i: 0 for i in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(fileSize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                fileSize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, fileSize)
        print_stats(stats, fileSize)
    except KeyboardInterrupt:
        print_stats(stats, fileSize)
        raise
