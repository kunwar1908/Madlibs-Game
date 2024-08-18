def get_input(word_type):
    return input(f"Enter a {word_type}: ")

def main():
    print("Welcome to Mad Libs!")
    
    noun = get_input("noun")
    verb = get_input("verb")
    adjective = get_input("adjective")
    adverb = get_input("adverb")

    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    print("Here is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()