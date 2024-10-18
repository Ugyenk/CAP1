# Read the input file

link = "https://csf101-server-cap1.onrender.com/get/input/337"
with open('input_text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()
    print('Downloaded: 337.txt')

import re

def is_dzongkha_word(word):
    # Assuming Dzongkha characters are within a specific Unicode range
    return re.match(r'^[\u0F00-\u0FFF]+$', word) is not None

def clean_dictionary(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    cleaned_words = [word.strip() for word in lines if is_dzongkha_word(word.strip())]
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_words))
    print(f"Cleaned dictionary saved to {output_file}")

input_file = 'dictionary1.txt'
output_file = 'cleaned_dictionary.txt'

clean_dictionary(input_file, output_file)


def load_dzongkha_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file.readlines())

def is_correct_word(word, dictionary):
    return word in dictionary

def spell_check(text, dictionary):
    words = re.findall(r'\b\w+\b', text)
    errors = [word for word in words if not is_correct_word(word, dictionary)]
    return errors

# Load the custom Dzongkha dictionary
dzongkha_dictionary = load_dzongkha_dictionary('cleaned_dictionary.txt')

# Read input text from a file
with open('input_text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

# Spell check
errors = spell_check(input_text, dzongkha_dictionary)
if errors:
    print("Spelling error:", errors)
else:
    print("No spelling error")
