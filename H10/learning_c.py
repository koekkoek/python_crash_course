from pathlib import Path

path = Path("learning_python.txt")
file = path.read_text().rstrip()
file = file.replace("Python", "C#")

print(file)
