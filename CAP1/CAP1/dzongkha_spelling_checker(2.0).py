##################################

#Ugyen Kinley Phuntshok
#A
#02240336

##################################

#Chat GPT, Youtube 
#https://www.python.org/
#Create a Dzongkha spell checker.
#https://www.youtube.com/results?search_query=how+to+create+a+spelling+checker+on+python

##################################

#Read the input file
import re
link = "https://csf101-server-cap1.onrender.com/get/input/337"
request_file = re.get(link)
with open('337.txt', 'wb') as file:
    data = file.write(request_file.content)
print('Downloaded: 337.txt')

import re

def load_dzongkha_dictionary(file_path):
    """
    Load Dzongkha words from a file into a set.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file.readlines())
    
#Check spelling
def is_correct_word(word, dictionary):
    """
    Check if a word exists in the dictionary.
    """
    return word in dictionary

def spell_check(text, dictionary):
    """
    Check the spelling of words in the text against the dictionary.
    """
    words = re.findall(r'\b\w+\b', text)
    errors = [word for word in words if not is_correct_word(word, dictionary)]
    return errors

# Load the custom Dzongkha dictionary
dzongkha_dictionary = load_dzongkha_dictionary('cleaned_dictionary.txt')

# Read input text from a file
with open('input_text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

# Main spell checking function
errors = spell_check(input_text, dzongkha_dictionary)
if errors:
    print("Spelling errors:", errors)
else:
    print("No spelling errors")

output=''
