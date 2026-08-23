import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am": "you are",
  "i was": "you were",
  "i": "you",
  "i'm": "you are",
  "i'd": "you would",
  "i've": "you have",
  "i'll": "you will",
  "my": "your",
  "you are": "I am",
  "you were": "I was",
  "you've": "I have",
  "you'll": "I will",
  "your": "my",
  "yours": "mine",
  "you": "me",
  "me": "you"
}

pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today ?"]],
    [r"hi|hey|hello", ["Hello", "Hey there"]],
    [r"what is your name ?", ["I am a bot created by Codingal Edu. pvt. Lim. you can call me Jarvis!"]],
    [r"how are you ?", ["I'm doing good. How about You ?"]],
    [r"sorry (.*)", ["Its alright", "Its OK, never mind"]],
    [r"I am fine", ["Great to hear that, How can I help you?"]],
    [r"i'm (.*) doing good", ["Nice to hear that", "How can I help you?:)"]],
    [r"(.*) age?", ["I'm a computer program dude. Seriously you are asking me this?"]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse"]],
    [r"(.*) created ?", ["Shravan created me using Python's NLTK library", "top secret ;)"]],
    [r"(.*) (location|city) ?", ["Bangalore, Karnataka"]],
    [r"how is weather in (.*)?", ["Weather in %1 is awesome like always"]],
    [r"quit", ["Bye take care. See you soon :)"]]
]

def chat():
    print("Hi! I am Jarvis.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()