#!/home/sobel/ros2_ws/.tensorflow1/bin/python3

import typer
from train import trainMain
from test import testApp

app = typer.Typer()

app.command("train")(trainMain)
app.command("test")(lambda: testApp())

if __name__ == "__main__":
    app()
