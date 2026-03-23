import datetime
import os

print("AI Agent Ready 😎 (type 'exit' to stop)")

while True:
    user_input = input("Tum: ").lower()

    if user_input == "exit":
        print("AI: Bye 👋")
        break

    elif "time" in user_input:
        print("AI:", datetime.datetime.now())

    elif "open notepad" in user_input:
        os.system("notepad")
        print("AI: Notepad open ho gaya")

    elif "calculate" in user_input:
        try:
            expr = user_input.replace("calculate", "")
            print("AI:", eval(expr))
        except:
            print("AI: Error hai")

    # 🔥 NEW ADD KAR
    elif "hello" in user_input or "hi" in user_input:
        print("AI: Hello bhai 😎")

    elif "how are you" in user_input:
        print("AI: Main mast hu, tu bata 😄")

    else:
        print("AI: Samajh nahi aaya 😅")
