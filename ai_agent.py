import requests

print("Real AI Ready 😎 (type 'exit' to stop)")

while True:
    user_input = input("Tum: ")

    if user_input.lower() == "exit":
        print("AI: Bye 👋")
        break

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": user_input,
                "stream": False
            }
        )

        data = response.json()
        print("AI:", data['response'])

    except:
        print("AI: Error aa gaya 😅 (check Ollama running hai ya nahi)")
