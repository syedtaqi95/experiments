from __future__ import annotations

from typing import Callable

import reactivex as rx
import reactivex.abc as rx_abc
from reactivex import operators as ops


def length_more_than_5() -> Callable[[rx.Observable[str]], rx.Observable[int]]:
    return rx.compose(
        ops.map(lambda s: len(s)),
        ops.filter(lambda i: i >= 5),  # noqa: PLR2004
    )


def lowercase() -> Callable[[rx.Observable[str]], rx.Observable[str]]:
    def _lowercase(source: rx.Observable[str]) -> rx.Observable[str]:
        def subscribe(
            observer: rx_abc.ObserverBase[str],
            scheduler: rx_abc.SchedulerBase | None = None,
        ) -> rx_abc.DisposableBase:
            def on_next(value: str) -> None:
                observer.on_next(value.lower())

            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler=scheduler,
            )

        return rx.create(subscribe)

    return _lowercase


def main() -> None:
    rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        lowercase(),
    ).subscribe(lambda value: print(f"Received {value}"))


if __name__ == "__main__":
    main()
