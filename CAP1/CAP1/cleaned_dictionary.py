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
