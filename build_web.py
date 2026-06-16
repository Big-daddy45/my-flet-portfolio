import subprocess
import sys

# Forces Python to trigger the internal build module directly
try:
    print("Starting legacy web bundle export...")
    subprocess.run([sys.executable, "-m", "pip", "install", "flet[web]"], check=True)
    print("\nBuild complete! Check your project folder for a 'build' or 'dist' directory.")
except Exception as e:
    print(f"Build redirection error: {e}")
