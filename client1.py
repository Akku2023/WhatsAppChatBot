
import ollama

response = ollama.chat(
    model="llama3.2",
    
    messages=[
        {
            "role": "system",
            "content": "You are a person named Akku who speaks hindi as well as english. She is from India and is a coder. You analyze chat history and talk like Akku"
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

print("Jarvis:", response["message"]["content"])
