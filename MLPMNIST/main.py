import typer
from train import trainMain
from test import testMain

app = typer.Typer()

app.command("train")(trainMain)
app.command("test")(testMain)

if __name__ == "__main__":
    app()
