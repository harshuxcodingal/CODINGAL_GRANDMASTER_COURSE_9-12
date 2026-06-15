print("===== AI ACTIVITIES =====")

print("\nAI Around Me")
ai_tools = ["Alexa", "Siri", "ChatGPT", "Netflix", "Google Maps"]

for tool in ai_tools:
    print(tool)

print("\nThings Translator")

translations = {
    "apple": "manzana",
    "dog": "perro",
    "cat": "gato"
}

word = input("Enter object: ")

if word in translations:
    print(translations[word])

print("\nQuick Draw")

drawing = input("What did you draw? ")
print("AI thinks it is:", drawing)