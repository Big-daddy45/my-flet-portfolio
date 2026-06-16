import flet.__init__ as flet
import flet.cli.commands.build as build
from flet.cli.cli import MainParser

print("Forcing Flet Web Build Compilation...")
try:
    # This forces Python to call the internal web compiler program directly
    build.Command().handle(MainParser(), ["web"])
    print("Successfully compiled! Check your folder sidebar for build/web/")
except Exception as e:
    print(f"Compilation stopped: {e}")