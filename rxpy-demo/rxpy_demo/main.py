from reactivex import of
from reactivex import operators as op


def main() -> None:
    of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        op.map(lambda s: len(s)),
        op.filter(lambda i: i >= 5),  # noqa: PLR2004
    ).subscribe(lambda value: print(f"Received {value}"))


if __name__ == "__main__":
    main()
