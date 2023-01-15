import pyttsx3
txs = pyttsx3.init()

""" RATE"""
rate = txs.getProperty('rate')   # getting details of current speaking rate                    #printing current voice rate
txs.setProperty('rate', 140)     # setting up new voice rate


"""VOLUME"""
volume = txs.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                     #printing current volume level
txs.setProperty('volume',50)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = txs.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
txs.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def txt_fun(text_input):
    print("speaking....")
    txs.say(text_input)
    txs.runAndWait()
    
txt = "Hello"
txt_fun(txt)

while txt != "bye":
    txt = input("what to speak: ")
    txt = txt.lower()
    txt_fun(txt)


