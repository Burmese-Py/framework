class BaseCommand:
  def handle_error(self, error):
    print(f"Erro: {error}")

class GenerateController(BaseCommand):
  command_name = "generate controller"
  description = "Generate a new controller"
  stub_path = "../../stubs/controller.py.jinja"

  def run(self, name):
    pass