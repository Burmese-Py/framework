from jinja2 import Environment, FileSystemLoader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

env = Environment(
  loader=FileSystemLoader(BASE_DIR)
)

def gen_model(name: str):
  template = env.get_template("models/model.py.jinja")
  loaded_template = template.render(name=name)

  with open(f"{name}.py", "w") as f:
    f.write(loaded_template)