import pyautogui
import time
import pyperclip
import ollama

# Keep fail-safe ON while developing
pyautogui.FAILSAFE = True


def is_last_message_from_sender(chat_log, sender_name="A Bestie"):
    """
    Check whether the copied chat contains the sender's name
    in the latest part of the conversation.
    """

    if not chat_log.strip():
        return False

    # Look at the last portion of the copied chat
    last_part = chat_log.strip()[-1000:]

    return sender_name.lower() in last_part.lower()


def generate_reply(chat_history):
    """
    Send the WhatsApp chat history to Ollama.
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are a person named Akanksha. "
                "You are from India and you are a coder. "
                "You speak Hindi and English. "
                "Talk naturally like Akanksha. "
                "Analyze the chat history and generate the next response. "
                "Output ONLY the text message. "
                "Do not include 'Akanksha:' or any explanation."
            )
        },
        {
            "role": "user",
            "content": chat_history
        }
    ]

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    return response["message"]["content"].strip()


# -------------------------------------------------
# IMPORTANT
# -------------------------------------------------
# Open WhatsApp first.
# Open the chat with "A Bestie".
# Put WhatsApp in the foreground.
# Then start this program.
# -------------------------------------------------

print("WhatsApp bot started.")
print("Make sure the A Bestie chat is open.")
print("Press Ctrl+C to stop.")

last_chat = ""

while True:

    try:
        # -----------------------------------------
        # Select chat text
        # -----------------------------------------

        pyautogui.moveTo(449, 110)

        pyautogui.dragTo(
            663,
            689,
            duration=1.0,
            button="left"
        )

        time.sleep(0.5)

        # -----------------------------------------
        # Copy selected text
        # -----------------------------------------

        pyautogui.hotkey("ctrl", "c")

        time.sleep(1)

        chat_history = pyperclip.paste()

        print("\n-------------------------")
        print("CHAT:")
        print(chat_history)
        print("-------------------------")

        # -----------------------------------------
        # Don't process the same chat repeatedly
        # -----------------------------------------

        if chat_history == last_chat:
            time.sleep(3)
            continue

        # -----------------------------------------
        # Check sender
        # -----------------------------------------

        if is_last_message_from_sender(
            chat_history,
            "A Bestie"
        ):

            print("Message from A Bestie detected.")

            # -------------------------------------
            # Generate AI response
            # -------------------------------------

            reply = generate_reply(chat_history)

            print("AI REPLY:")
            print(reply)

            # -------------------------------------
            # Copy reply
            # -------------------------------------

            pyperclip.copy(reply)

            time.sleep(0.5)

            # -------------------------------------
            # CLICK THE WHATSAPP MESSAGE BOX
            #
            # YOU MUST CHANGE THESE COORDINATES
            # TO THE MESSAGE BOX ON YOUR SCREEN.
            # -------------------------------------

            pyautogui.click(600, 700)

            time.sleep(0.5)

            # Paste response
            pyautogui.hotkey("ctrl", "v")

            time.sleep(0.5)

            # Send
            pyautogui.press("enter")

            print("Reply sent!")

            # Remember this chat so we don't reply again
            last_chat = chat_history

            time.sleep(3)

        else:
            print("No new message from A Bestie.")

        time.sleep(3)

    except KeyboardInterrupt:

        print("\nBot stopped.")
        break

    except Exception as e:

        print("ERROR:", e)
        time.sleep(3)