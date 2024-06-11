from reactivex import of


def main() -> None:
    source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

    source.subscribe(
        on_next=lambda i: print(f"Received {i}"),
        on_error=lambda e: print(f"Error occurred: {e}"),
        on_completed=lambda: print("Done!"),
    )


if __name__ == "__main__":
    main()
