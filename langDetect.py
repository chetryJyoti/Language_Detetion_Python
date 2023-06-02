# Import the detect function from langdetect
from langdetect import detect
from languageNames import language_names


def detect_language(sentence, n):
    try:
        if sentence[n]:
            new_sentence = sentence[n].strip('\n')
            lang_code = detect(new_sentence)
            lang_name = language_names.get(lang_code, 'Unknown')
            print(
                f'The language for the sentence "{new_sentence}" is {lang_name} ({lang_code})')

    except:
        print('Sentence does not exist')


# Open the sentences.txt file in read mode
with open('sentences.txt', 'r', encoding='utf-8') as sentences_file:
    # Read all the lines from the file and store them in a list
    sentences = sentences_file.readlines()

    # Print the number of sentences in the file
    print(f'You have {len(sentences)} sentences')

    # Prompt the user to enter an integer representing the sentence index
    number_of_sentence = int(
        input('Which sentence do you want to detect? (Provide an integer please): '))

    # Call the detect_language function to detect the language of the specified sentence
    detect_language(sentences, number_of_sentence)
