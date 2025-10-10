# 6 The I/O Loop
    # Creating a basic chatbot that interacts with user in continuous loop until they type "exit"

import nltk

def process(user_input):
    tokens = nltk.word_tokenize(user_input)
    return tokens

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        processed_input = process(user_input)
        print(f"Bot: You said {processed_input}")

if __name__ == "__main__":
    main()