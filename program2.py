# import pyautogui
# import time
# import pyperclip
# import ollama

# pyautogui.FAILSAFE = False


# def is_last_message_from_sender(chat_log, sender_name="Meta AI"):
#     """
#     Check whether the latest part of the copied chat contains
#     a message from Meta AI.
#     """

#     if not chat_log:
#         return False

#     # Split into lines and remove empty lines
#     lines = [line.strip() for line in chat_log.splitlines() if line.strip()]

#     if not lines:
#         return False

#     # Check the last occurrence of sender name
#     return sender_name.lower() in lines[-1].lower()


# # Open Chrome
# pyautogui.click(1366, 768)
# time.sleep(2)


# last_chat_history = ""

# while True:

#     # -------------------------------
#     # SELECT CHAT HISTORY
#     # -------------------------------

#     pyautogui.moveTo(520, 200, duration=0.5)
#     time.sleep(0.5)

#     pyautogui.mouseDown()
#     time.sleep(0.3)

#     pyautogui.moveTo(663, 689, duration=2.0)

#     time.sleep(0.3)
#     pyautogui.mouseUp()

#     time.sleep(1)

#     # -------------------------------
#     # COPY
#     # -------------------------------

#     pyautogui.hotkey("ctrl", "c")
#     time.sleep(1)

#     chat_history = pyperclip.paste()

#     print("\n---------------- CHAT HISTORY ----------------")
#     print(chat_history)
#     print("----------------------------------------------\n")

#     # Don't process exactly the same chat repeatedly
#     if chat_history == last_chat_history:
#         time.sleep(2)
#         continue

#     # -------------------------------
#     # CHECK LAST MESSAGE
#     # -------------------------------

#     if is_last_message_from_sender(chat_history, "Meta AI"):

#         print("Meta AI message detected!")

#         # -------------------------------
#         # CREATE OLLAMA MESSAGES
#         # -------------------------------

#         messages = [
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a person named Akanksha Mali who speaks "
#                     "Hindi, Marathi as well as English. You are from India "
#                     "and you are a coder. Analyze the chat history and "
#                     "reply naturally like Akanksha Mali. "
#                     "Output ONLY the next chat response as a text message. "
#                     "Do not explain your reasoning."
#                 )
#             },
#             {
#                 "role": "user",
#                 "content": chat_history
#             }
#         ]

#         # -------------------------------
#         # CALL OLLAMA
#         # -------------------------------

#         print("Sending chat history to Ollama...")

#         try:
#             response = ollama.chat(
#                 model="llama3.2",
#                 messages=messages
#             )

#             reply = response["message"]["content"].strip()

#             print("Ollama reply:")
#             print(reply)

#         except Exception as e:
#             print("Ollama ERROR:", e)
#             time.sleep(3)
#             continue

#         # -------------------------------
#         # COPY REPLY
#         # -------------------------------

#         pyperclip.copy(reply)

#         # -------------------------------
#         # CLICK MESSAGE INPUT
#         # -------------------------------

#         pyautogui.click(578, 689)
#         time.sleep(0.5)

#         # -------------------------------
#         # PASTE REPLY
#         # -------------------------------

#         pyautogui.hotkey("ctrl", "v")
#         time.sleep(0.5)

#         # -------------------------------
#         # SEND
#         # -------------------------------

#         pyautogui.press("enter")

#         print("Reply sent!")

#         # Remember this chat so it doesn't immediately reply again
#         last_chat_history = chat_history

#         # Give website time to update
#         time.sleep(3)

#     else:
#         print("Last message is not from Meta AI.")

#     time.sleep(2)

# import pyautogui
# import time
# import pyperclip

# pyautogui.FAILSAFE = False

# while True:

#     # Select chat
#     pyautogui.moveTo(520, 200, duration=0.5)
#     pyautogui.mouseDown()
#     pyautogui.moveTo(663, 689, duration=2)
#     pyautogui.mouseUp()

#     time.sleep(1)

#     # Copy
#     pyautogui.hotkey("ctrl", "c")
#     time.sleep(1)

#     chat_history = pyperclip.paste()

#     print("\n==============================")
#     print("COPIED CHAT:")
#     print(repr(chat_history))
#     print("==============================")

#     # Don't check only the last line.
#     if "Meta AI" in chat_history:
#         print(">>> META AI FOUND <<<")
#     else:
#         print(">>> META AI NOT FOUND <<<")

#     time.sleep(3)

import pyautogui
import time
import pyperclip
import ollama

pyautogui.FAILSAFE = False


# ============================================================
# COPY CHAT
# ============================================================

def get_chat_history():

    # Click/drag to select chat
    pyautogui.moveTo(520, 200, duration=0.5)

    pyautogui.mouseDown()
    time.sleep(0.3)

    pyautogui.moveTo(663, 689, duration=2)

    pyautogui.mouseUp()

    time.sleep(0.8)

    # Clear clipboard
    pyperclip.copy("")

    # Copy
    pyautogui.hotkey("ctrl", "c")

    time.sleep(1)

    return pyperclip.paste()


# ============================================================
# ASK OLLAMA
# ============================================================

def generate_reply(chat_history):

    messages = [
        {
            "role": "system",
            "content": """
You are Akanksha Mali.

You are a person from India who speaks Hindi, Marathi and English.

You are a normal person.

You are chatting casually with another person.

Analyze the complete conversation and write the next message
that Akanksha should send.

Be natural and conversational.

Output ONLY the message.

Do not explain your reasoning.
Do not say "Akanksha:".
Do not put the response inside quotation marks.
"""
        },
        {
            "role": "user",
            "content": chat_history
        }
    ]

    try:

        print("\nSending conversation to Ollama...")

        response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        reply = response["message"]["content"].strip()

        return reply

    except Exception as e:

        print("\nOLLAMA ERROR:")
        print(e)

        return None


# ============================================================
# MAIN
# ============================================================

print("Starting program...")

previous_history = ""

# ------------------------------------------------------------
# IMPORTANT:
#
# The first message in your copied chat is YOUR message.
#
# Therefore we initially assume:
#
# message 1 = YOU
#
# We keep track of the conversation ourselves.
# ------------------------------------------------------------

last_sender = "you"


while True:

    try:

        # ----------------------------------------------------
        # GET CHAT
        # ----------------------------------------------------

        chat_history = get_chat_history()

        if not chat_history.strip():

            print("Clipboard empty. Retrying...")

            time.sleep(2)

            continue


        print("\n========================================")
        print("CHAT HISTORY")
        print("========================================")

        print(chat_history)

        print("========================================")


        # ----------------------------------------------------
        # FIRST RUN
        # ----------------------------------------------------

        if previous_history == "":

            previous_history = chat_history

            print("Initial chat loaded.")

            time.sleep(3)

            continue


        # ----------------------------------------------------
        # NO CHANGE
        # ----------------------------------------------------

        if chat_history == previous_history:

            print("No new message.")

            time.sleep(2)

            continue


        # ----------------------------------------------------
        # CHAT CHANGED
        # ----------------------------------------------------

        print("\nNEW CHAT CONTENT DETECTED!")


        # Get individual messages

        messages = [
            line.strip()
            for line in chat_history.splitlines()
            if line.strip()
        ]


        # ----------------------------------------------------
        # GET LAST MESSAGE
        # ----------------------------------------------------

        newest_message = messages[-1]

        print("\nLatest message:")
        print(newest_message)


        # ----------------------------------------------------
        # DETERMINE NEW SENDER
        # ----------------------------------------------------

        if last_sender == "you":

            new_sender = "Mummy"

        else:

            new_sender = "you"


        print("Detected sender:", new_sender)


        # ----------------------------------------------------
        # IF META AI SENT MESSAGE
        # ----------------------------------------------------

        if new_sender == "Mummy":

            print("\nMummy message detected!")

            reply = generate_reply(chat_history)

            if reply is None:

                print("Ollama didn't return a reply.")

                time.sleep(2)

                continue


            print("\nAI REPLY:")
            print(reply)


            # ------------------------------------------------
            # COPY REPLY
            # ------------------------------------------------

            pyperclip.copy(reply)

            time.sleep(0.5)


            # ------------------------------------------------
            # CLICK INPUT
            # ------------------------------------------------

            pyautogui.click(578, 689)

            time.sleep(0.5)


            # ------------------------------------------------
            # PASTE
            # ------------------------------------------------

            pyautogui.hotkey("ctrl", "v")

            time.sleep(0.5)


            # ------------------------------------------------
            # SEND
            # ------------------------------------------------

            pyautogui.press("enter")

            print("\nREPLY SENT!")


            # We just sent the message
            last_sender = "you"

        else:

            print("Latest message was sent by you.")

            last_sender = "you"


        # ----------------------------------------------------
        # SAVE CURRENT CHAT
        # ----------------------------------------------------

        previous_history = chat_history


        time.sleep(4)


    except KeyboardInterrupt:

        print("\nProgram stopped.")

        break




    except Exception as e:

        print("\nPROGRAM ERROR:")
        print(e)

        time.sleep(3)
        