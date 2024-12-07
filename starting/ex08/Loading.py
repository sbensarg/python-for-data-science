import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 60

    for i, elem in enumerate(lst):
        percent = (i + 1) / total * 100
        filled_length = int(bar_length * percent // 100)
        bar = (
            '=' * filled_length + '>' + '.' * (bar_length - filled_length - 1)
        )
        sys.stdout.write(f'\r[{bar}] {i + 1}/{total} | {percent:.2f}%')
        sys.stdout.flush()
        yield elem
    sys.stdout.write('\n')
