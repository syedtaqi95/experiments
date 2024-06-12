from __future__ import annotations

import asyncio
import multiprocessing
import random
import time
from threading import current_thread
from typing import Any, Callable, NamedTuple

import reactivex as rx
import reactivex.abc as rx_abc
from reactivex import operators as ops
from reactivex.scheduler import ThreadPoolScheduler
from reactivex.scheduler.eventloop import AsyncIOScheduler
from reactivex.subject import Subject


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


# IO Concurrency
class EchoItem(NamedTuple):
    future: asyncio.Future[str]
    data: str


class AsyncioTaskDisposable(rx_abc.DisposableBase):
    def __init__(self: AsyncioTaskDisposable, task: asyncio.Task) -> None:
        self.task = task

    def dispose(self: AsyncioTaskDisposable) -> None:
        if not self.task.done():
            self.task.cancel()


def tcp_server(
    sink: rx.Observable[EchoItem],
    loop: asyncio.AbstractEventLoop,
) -> rx.Observable[EchoItem]:
    def on_subscribe(
        observer: rx_abc.ObserverBase[EchoItem],
        _: rx_abc.SchedulerBase | None,
    ) -> rx_abc.DisposableBase:
        async def handle_echo(
            reader: asyncio.StreamReader,
            writer: asyncio.StreamWriter,
        ) -> None:
            print("new client connected")
            while True:
                data = await reader.readline()
                data = data.decode("utf-8")
                if not data:
                    break

                future: asyncio.Future[str] = asyncio.Future()
                observer.on_next(
                    EchoItem(
                        future=future,
                        data=data,
                    ),
                )
                await future
                writer.write(future.result().encode("utf-8"))

            print("Close the client socket")
            writer.close()
            await writer.wait_closed()

        def on_next(i: EchoItem) -> None:
            i.future.set_result(i.data)

        print("starting server")
        server = asyncio.start_server(handle_echo, "127.0.0.1", 8888)
        task = loop.create_task(server)

        sink.subscribe(
            on_next=on_next,
            on_error=observer.on_error,
            on_completed=observer.on_completed,
        )

        return AsyncioTaskDisposable(task)

    return rx.create(on_subscribe)


def io_concurrency() -> None:
    loop = asyncio.new_event_loop()
    proxy = Subject()
    source = tcp_server(proxy, loop)
    aio_scheduler = AsyncIOScheduler(loop=loop)

    source.pipe(
        ops.map(lambda i: i._replace(data=f"echo: {i.data}")),
        ops.delay(5.0),
    ).subscribe(proxy, scheduler=aio_scheduler)

    loop.run_forever()
    print("done")
    loop.close()


def main() -> None:
    # chaining_operators()
    # custom_operator()
    # cpu_concurrency()
    io_concurrency()


if __name__ == "__main__":
    main()
