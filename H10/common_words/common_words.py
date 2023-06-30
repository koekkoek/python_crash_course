from pathlib import Path


def count_words(word):
    books = [
        "alice_in_wonderland.txt",
        "dorienboek.txt",
        "moby_dick.txt",
        "romeo_and_juliet.txt",
    ]

    for book in books:
        path = Path(book)
        print(f"\nSearching in {book} for the following word: '{word.strip()}.'")
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print("No file found.")
        else:
            print(f"We count {text.lower().count(word)} the word '{word.strip()}.'")


count_words(" the ")
