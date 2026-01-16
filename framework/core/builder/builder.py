from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import secrets, re
from datetime import datetime

BASE_PATH = Path(__file__).resolve().parent.parent.parent / "templates" / "project"
env = Environment(loader=BASE_PATH)

def initialize(name: str):
  DESTINATION_PATH = Path.cwd()

  context = {
    "project_name": _to_snake_case(name),
    "app_key": secrets.token_urlsafe(32),
    "created_at": datetime.now().isoformat(),

    "class_name": _to_pascal_case(name)
  }

  template_dir = BASE_PATH

  for item in template_dir.rglob("*"):
    relative_path = item.relative_to(template_dir)
    target_path = DESTINATION_PATH / relative_path

    if item.is_dir():
      target_path.mkdir(parents=True, exist_ok=True)
    else:
      template_content = item.read_text()
      rendered_content = env.from_string(template_content).render(context)

      final_path = target_path.with_suffix('') if target_path.suffix == '.jinja' else target_path
      final_path.write_text(rendered_content)


def _to_pascal_case(string: str):
  splited_str = re.split(r"\W+", string)

  for word in range(len(splited_str)):
    splited_str[word] = splited_str[word].capitalize()

  return ''.join(splited_str)

def _to_snake_case(string: str):
  splited_str = re.split(r"\W+", string)

  return ''.join(splited_str)