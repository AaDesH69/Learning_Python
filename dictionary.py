english_nepali_dict = {
    "good": "राम्रो (ramro)",
    "bad": "नराम्रो (naramro)",
    "hello": "नमस्कार (namaste)",
    "goodbye": "अलविदा (alvida)",
    "thank you": "धन्यवाद (dhanyabad)",
    "school": "विद्यालय (Vidyālaya)",
    "home": "घर (ghar)",
    "yes": "हो (ho)",
    "no": "छैन (Chaina)",
    "friend": "मित्र (mitra)",
    "child": "बच्चा (bachcha)",
    "father": "बुबा (Buwa)"
}


def add_word(english_word, nepali_word):
    try:
        # Convert to lowercase for case-insensitive matching
        english_word = english_word.lower()

        if english_word not in english_nepali_dict:
            english_nepali_dict[english_word] = nepali_word
            print(f"Word '{english_word}' added to the dictionary!")
        else:
            print(f"Word '{english_word}' already exists in the dictionary.")
    except Exception as e:
        print(f"An error occurred: {e}")


def translate(english_word):
    try:
        # Convert to lowercase for case-insensitive matching
        english_word = english_word.lower()

        nepali_word = english_nepali_dict.get(english_word)
        if nepali_word:
            return nepali_word
        else:
            return "Word not found"
    except Exception as e:
        print(f"An error occurred: {e}")


def list_words():
    """
    Prints a list of all translatable English words in the dictionary.
    """
    if english_nepali_dict:
        print("\nList of Translatable Words:")
        for english_word in english_nepali_dict.keys():
            print(english_word)
    else:
        print("The dictionary is currently empty!")


# Main program loop
while True:
    print("\nEnglish-Nepali Dictionary")
    print("1. Add Word")
    print("2. Translate English to Nepali")
    print("3. List Translatable Words")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        try:
            english_word = input("Enter English word: ")
            nepali_word = input("Enter Nepali translation: ")
            add_word(english_word, nepali_word)
        except Exception as e:
            print(f"An error occurred while adding the word: {e}")
    elif choice == '2':
        try:
            english_word = input("Enter English word to translate: ")
            nepali_translation = translate(english_word)
            print(f"Translation: {nepali_translation}")
        except Exception as e:
            print(f"An error occurred during translation: {e}")
    elif choice == '3':
        list_words()
    elif choice == '4':
        print("Exiting the program!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
