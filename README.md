# WhatsAppChatBot

# AI Chat Automation Using Python and Ollama

## 📌 Project Overview

This project is an AI-powered chat automation program built using Python, PyAutoGUI, Pyperclip, and Ollama. It reads chat history from a chat window, detects new messages, generates a natural and conversational reply using the Llama 3.2 model, and automatically sends the generated response through the chat interface.

The AI is prompted to respond as **Akanksha Mali**, communicating naturally in Hindi, Marathi, and English.

## ✨ Features

- **Automated Chat Reading:** Selects and copies chat history from the active chat window.
- **New Message Detection:** Checks whether the conversation has changed.
- **AI-Powered Replies:** Uses Ollama with the `llama3.2` model to generate responses.
- **Automatic Message Sending:** Copies the AI-generated reply, pastes it into the chat input, and sends it.
- **Continuous Monitoring:** Repeatedly checks for new messages while the program is running.
- **Error Handling:** Handles Ollama errors, unexpected exceptions, and keyboard interruption.
- **Multilingual Conversation:** Prompts the AI to generate natural replies in Hindi, Marathi, and English.

## 🛠️ Technologies Used

- **Python** — Core programming language.
- **PyAutoGUI** — Automates mouse and keyboard interactions.
- **Pyperclip** — Reads from and writes to the system clipboard.
- **Ollama** — Runs the local language model.
- **Llama 3.2** — Generates conversational responses.

## 📋 Prerequisites

Before running the project, make sure you have:

1. Python installed on your system.
2. Ollama installed and running.
3. The `llama3.2` model downloaded.
4. Google Chrome or another compatible browser with the chat interface open.
5. An active chat window with the expected layout.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Replace the repository URL and project folder with your actual details.

### 2. Install Python Dependencies

Run the following command in your terminal:

```bash
pip install pyautogui pyperclip ollama
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com/download

### 4. Download the Llama 3.2 Model

Open a terminal and run:

```bash
ollama pull llama3.2
```

Make sure Ollama is running before starting the Python program.

### 5. Configure the Chat Window

- Open Chrome and navigate to your chat interface.
- Open the conversation you want to monitor.
- Make sure the chat history and message input are visible.
- Ensure the mouse coordinates used in the script match your screen layout.

**Note:** The current script uses fixed screen coordinates, so changing the window size, display scaling, or chat layout may require updating the coordinates in the code.

## ▶️ How to Run the Program

To execute the project and get the output, run **`program2.py`**.

Open a terminal in the project directory and execute:

```bash
python program2.py
```

If your system uses `python3` instead, run:

```bash
python3 program2.py
```

Keep the chat window open and make sure it is positioned correctly while the program is running.

## 📤 Expected Output

When the program starts, the terminal displays:

```text
Starting program...
```

It then copies and displays the current chat history:

```text
========================================
CHAT HISTORY
========================================
[Your existing chat conversation]
========================================
Initial chat loaded.
```

When a change is detected in the conversation, the program displays the latest message and its inferred sender:

```text
NEW CHAT CONTENT DETECTED!

Latest message:
Mummy: Hi, how are you?

Detected sender: Mummy

Mummy message detected!

Sending conversation to Ollama...

AI REPLY:
I'm good! How are you?
```

The generated response is then pasted into the chat input and sent automatically. The terminal displays:

```text
REPLY SENT!
```

The exact AI-generated reply will vary depending on the conversation.

## ⚙️ How the Program Works

1. **Start:** Initializes the automation and sets up conversation tracking.
2. **Copy Chat History:** Uses PyAutoGUI to select the chat and Pyperclip to copy its contents.
3. **Check for Changes:** Compares the copied chat history with the previous version.
4. **Identify the Latest Message:** Extracts the last non-empty line from the copied conversation.
5. **Generate a Reply:** Sends the conversation history to the Llama 3.2 model through Ollama.
6. **Send the Reply:** Copies the generated text, pastes it into the chat input, and presses Enter.
7. **Repeat:** Continues monitoring the conversation until manually stopped.

## 🛑 Stop the Program

To stop execution, press:

```text
Ctrl + C
```

The program catches the keyboard interruption and displays:

```text
Program stopped.
```

## ⚠️ Important Notes

- The program runs continuously until stopped manually.
- Keep the browser window active and the chat interface visible.
- The mouse coordinates in the script are fixed and may need adjustment for your screen.
- The script assumes messages alternate between you and the other participant. This sender-detection logic may not work correctly for every chat interface or conversation.
- The program may send incorrect or unintended responses. Review the automation carefully and test it in a safe environment before using it with real conversations.
- `pyautogui.FAILSAFE = False` disables PyAutoGUI's corner-based emergency stop. Consider enabling the failsafe during testing.
- The first copied chat history is used for initialization, so the program does not immediately respond to the existing conversation.

## 🔒 Privacy

Ollama can run the language model locally, which helps keep conversation processing on your own machine. However, the automation interacts with a third-party chat interface, and privacy depends on the services and configuration you use. Avoid processing sensitive conversations without appropriate permission.

## 📁 Project Structure

```text
project-folder/
│
├── program2.py       # Main chat automation program
└── README.md          # Project documentation
```

## 👨‍💻 Author

**Akanksha Mali**

## 📄 License

Add a license to this project if you intend to distribute or publish it publicly.
