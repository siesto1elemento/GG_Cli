import typer

app = typer.Typer()

@app.command()
def main(name : str):
    print(f"hello {name}")

@app.command()
def greet(name: str, formal:bool = False):
    if formal:
        print(f"how is your day going mr/miss {name}")
    else:
        print(f"hi {name}")


if __name__ == "__main__":
    app()