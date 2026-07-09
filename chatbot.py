import nltk
from nltk.chat.util import Chat, reflections

# Pehli baar run karte waqt ye line use karo
nltk.download('punkt')

# Chatbot ke questions aur answers
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! Kaise ho?", "Hi! Main aapki help ke liye yahan hoon."]
    ],
    [
        r"what is your name ?",
        ["Mera naam EliteTech Chatbot hai."]
    ],
    [
        r"how are you ?",
        ["Main bilkul theek hoon. Aap kaise hain?"]
    ],
    [
        r"who created you ?",
        ["Mujhe Python aur NLTK se banaya gaya hai."]
    ],
    [
        r"bye",
        ["Bye! Have a great day."]
    ]
]

# Chatbot start
chatbot = Chat(pairs, reflections)

print("===================================")
print(" AI Chatbot with NLP")
print(" Type 'bye' to exit")
print("===================================")

chatbot.converse()