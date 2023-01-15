from nltk.chat.util import Chat,reflections
pairs =[
    [r"hi|hey|hello",['hii']],
]
chat = Chat(pairs,reflections)
chat.converse()
def quit1():
    print("hii I am Chatbot ask me anything")
if __name__ =="__main__":
    quit1()