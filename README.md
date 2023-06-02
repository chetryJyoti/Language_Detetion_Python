# Language Detetion using Python
 Code to detect language using langdetect library

- **This repo contains 3 files langDetect.py, languageNames.py, and sentences.txt.** 
- **Here's an explanation of how the code works with these files:**
- The langDetect.py file contains the main code logic for language detection.
- The languageNames.py file contains the language_names dictionary, which maps language codes to their names.
- The sentences.txt file contains the sentences to detect the languages.
- The code in langDetect.py opens the sentences.txt file, reads the sentences, and stores them in a list called sentences.
- The user is prompted to enter the index of the sentence they want to detect the language for.
- The code calls the detect_language function, which uses the langdetect module to detect the language of the specified sentence. It then uses the language_names dictionary to map the language code to its name.
- The detected language name and code are printed in the format "The language for the sentence 'sentence' is language_name - language_code".
