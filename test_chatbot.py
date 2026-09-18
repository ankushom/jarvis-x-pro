from chatbot import ask_ai

while True:

    q = input("You : ")

    if q == "exit":
        break

    print()

    print(ask_ai(q))

    print()