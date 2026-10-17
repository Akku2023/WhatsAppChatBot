import pyautogui
import time
import pyperclip
import ollama

# response = ollama.chat(
#     model="llama3.2",
#     # messages = messages
# )
    
pyautogui.FAILSAFE = False

def is_last_message_from_sender(chat_log, sender_name="Meta AI"):
    #split the chat log into individual messages
    messages = chat_log.strip().split("/2026")[-1]
    if sender_name in messages:
        return True
    return False
    
    #iterate through the message in reverse to find the last message
    # for message in reversed(messages):
    #     #split each message by ":", which separates the timestamp, sender, and content
    #     parts = message.split(":", 2)
    #     if len(parts) >=3:
    #         timestamp, sender, content = parts
    #         # check if the sender of the last message is the specified sender
    #         if sender.strip()== sender_name:
    #             return True
    #         else:
    #             return False
            
    # return False
    #step1: click on the chrome icon at coordinates (1366, 768)
pyautogui.click(1366, 768)
time.sleep(1) #wait for 1 second to ensure the click is registered
'''

while True:
    
    #step2: drag the mouse from (582, 634) to (663, 689) to select the text
    pyautogui.moveTo(520, 200)
    pyautogui.dragTo(663, 689, duration=1.0, button='left') #drag for 1 second

    #step3: copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(24, 537)
    time.sleep(2) #wait for 1 second to ensure the copy command is completed

    #step4: retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    #print the copied text to verify
    print(chat_history)
    
    if is_last_message_from_sender(chat_history):

             #model="llama3.2",
                    
            messages=[
                        {
                            "role": "system",
                            "content": "You are a person named Akanksha who speaks hindi, marathi as well as english. You are from India and you are a coder. You analyze chat history and talk like Akanksha. Output should be the next chat response (text message only)."
                        },
                        {
                            "role": "user",
                            "content": chat_history
                        }
                    ]
            response = ollama.chat(
    model="llama3.2",
    messages = messages
)
                

            reply = response["message"]["content"]
            pyperclip.copy(reply)

            #step5: click at cooredinates (578, 689)
            pyautogui.click(578, 689)
            time.sleep(1) #wait for 1 second to ensure the click is registered

            #step6: paste the text
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1) #wait for 1 second to ensure the paste command is completed

            #step7: press enter
            pyautogui.press('enter')
          '''  
         
while True:

    # Select chat text
    pyautogui.moveTo(520, 200, duration=0.5)
    time.sleep(0.5)

    pyautogui.mouseDown()
    time.sleep(0.3)

    pyautogui.moveTo(663, 689, duration=2.0)

    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(1)

    # Copy
    pyautogui.hotkey('ctrl', 'c')
    
    time.sleep(1)

    chat_history = pyperclip.paste()

    print(chat_history)

    if is_last_message_from_sender(chat_history):
        
        # response = ollama.chat(
        #     model="llama3.2",
        #             # messages=messages
        # )

        messages =[
            {
                "role": "system",
                "content": "You are a person named Akanksha Mali who speaks Hindi, Marathi as well as English. You are from India and you are a coder. Analyze chat history and talk like Akanksha Mali. Output should be the next chat response (text message only)."
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

        reply = response["message"]["content"]

        pyperclip.copy(reply)

        # Click message input
        pyautogui.click(578, 689)
        time.sleep(0.5)

        # Paste
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)



        # Send
        pyautogui.press('enter')
        
    