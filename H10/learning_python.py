from pathlib import Path

path = Path("learning_python.txt")
text = path.read_text().rstrip()

# First attempt. Reading complete file.
print(text, end="\n\n")

# Seconde attempt. Line by line.
for line in text.splitlines():
    print("Michel said: '" + line + "'")
