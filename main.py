import random
username=input("\n\nPlease enter your name: ")
print(f"\nHello {username}. This is a chat-bot made using Python.")
input_coms=input("\nPlease say hello.\n\nYou:  ")

#basic communication function
def basic_coms(input_coms,username):
    print(f"\nj-bot: Hello there {username}. Are you feeling good today?? (yes/no)")
    feelingInput=input("\nYou: ")
    if feelingInput.lower()=="yes":
        print("\nj-bot: Glad to hear that. Spread the positive vibes 😉")


if input_coms.lower()=="hello":
    basic_coms(input_coms,username)
else:
    print("Sorry my model is not trained enough to operate on that input")

