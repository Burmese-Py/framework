import typer
from framework.templates.generator import runner

app = typer.Typer()

@app.command()
def generate(nome: str):
  runner.gen_model(nome)

@app.command()
def version():
  print("v0.1.0")

def main():
  app()

if __name__ == "__main__":
  main()