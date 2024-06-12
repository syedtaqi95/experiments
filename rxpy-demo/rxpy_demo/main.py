from __future__ import annotations

import multiprocessing
import random
import time
from threading import current_thread
from typing import Any, Callable

import reactivex as rx
import reactivex.abc as rx_abc
from reactivex import operators as ops
from reactivex.scheduler import ThreadPoolScheduler


# Chaining operators
def length_more_than_5() -> Callable[[rx.Observable[str]], rx.Observable[int]]:
    return rx.compose(
        ops.map(lambda s: len(s)),
        ops.filter(lambda i: i >= 5),  # noqa: PLR2004
    )


def chaining_operators() -> None:
    rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        length_more_than_5(),
    ).subscribe(lambda value: print(f"Received {value}"))


# Custom operator
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


def custom_operator() -> None:
    rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        lowercase(),
    ).subscribe(lambda value: print(f"Received {value}"))


# CPU Concurrency
def intense_calculation(value: Any) -> None:  # noqa: ANN401
    time.sleep(random.randint(5, 20) * 0.1)  # noqa: S311
    return value


def cpu_concurrency() -> None:
    optimal_thread_count = multiprocessing.cpu_count()
    pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

    # Create process 1
    rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        ops.map(lambda s: intense_calculation(s)),
        ops.subscribe_on(pool_scheduler),
    ).subscribe(
        on_next=lambda s: print(f"PROCESS 1: {current_thread().name} {s}"),
        on_error=lambda e: print(e),
        on_completed=lambda: print("PROCESS 1 done"),
    )

    # Create process 2
    rx.range(1, 10).pipe(
        ops.map(lambda s: intense_calculation(s)),
        ops.subscribe_on(pool_scheduler),
    ).subscribe(
        on_next=lambda s: print(f"PROCESS 2: {current_thread().name} {s}"),
        on_error=lambda e: print(e),
        on_completed=lambda: print("PROCESS 2 done"),
    )

    # Create process 3, which is infinite
    rx.interval(1).pipe(
        ops.map(lambda i: i * 100),
        ops.observe_on(pool_scheduler),
        ops.map(lambda s: intense_calculation(s)),
    ).subscribe(
        on_next=lambda i: print(f"PROCESS 3: {current_thread().name} {i}"),
        on_error=lambda e: print(e),
    )

    input("Press Enter key to exit\n")


def main() -> None:
    # chaining_operators()
    # custom_operator()
    cpu_concurrency()


if __name__ == "__main__":
    main()
