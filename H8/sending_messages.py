def send_messages(messages, sent_messages):
    while messages:
        new_msg = messages.pop()
        print(f"New text message: {new_msg}")
        sent_messages.append(new_msg)


def processed_messages(sent_messages):
    print("\nThe following messages are printed:")
    for msg in sent_messages:
        print(f"* {msg}")


msg = [
    "I don't like an apple.",
    "Well, it's just who I am.",
    "Think of me as a banana.",
    "Some strange things will hapen",
]
sent_messages = []

send_messages(msg, sent_messages)
processed_messages(sent_messages)
