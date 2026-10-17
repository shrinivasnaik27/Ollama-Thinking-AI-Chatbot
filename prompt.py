
from ollama import Client

# Initialize Ollama client
client = Client(host="http://localhost:11434")

MODEL = "qwen3.5:0.8b"

print("===================================")
print("       OLLAMA AI CHATBOT")
print("===================================")
print("Model:", MODEL)
print("Type 'exit' to quit.\n")

while True:
    question = input("User: ").strip()

    if question.lower() in ("exit", "quit"):
        print("AI: Goodbye!")
        break

    if not question:
        print("Please enter a question.\n")
        continue

    # Choose thinking mode
    mode = input("Enable thinking? (true/false): ").strip().lower()

    if mode not in ("true", "false"):
        print("Please enter true or false.\n")
        continue

    think = mode == "true"

    # Choose temperature
    try:
        temperature = float(
            input("Temperature (0 to 2): ").strip()
        )

        if not 0 <= temperature <= 2:
            print("Temperature must be between 0 and 2.\n")
            continue

    except ValueError:
        print("Please enter a valid number, such as 0, 0.8, 1 or 2.\n")
        continue

    try:
        print("\nGenerating response...")

        completion = client.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Give a clear, useful answer to the user. "
                        "Use simple language. Avoid bullet points "
                        "unless they improve the explanation."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            think=think,
            options={
                "temperature": temperature,
                "num_predict": 1024
            },
            stream=False
        )

        message = completion.message

        # Show thinking separately when enabled
        thinking_text = getattr(message, "thinking", None)
        answer = (message.content or "").strip()

        if think and thinking_text:
            print("\n--- Thinking output ---")
            print(thinking_text)

        # Show the final answer
        print("\n--- AI Response ---")

        if answer:
            print(answer)
        else:
            print("The model returned no final answer.")
            print("Try a shorter question or check the model version.")

        print("\n" + "=" * 35 + "\n")

    except Exception as error:
        print("\nSomething went wrong:", error)
        print("Check that Ollama is running and the model is installed.\n")
