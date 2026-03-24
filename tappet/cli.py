import click

from tappet.app import TappetApp


@click.command()
def main() -> None:
    """Run the tappet TUI application."""
    app = TappetApp()
    app.run()


if __name__ == "__main__":
    main()
