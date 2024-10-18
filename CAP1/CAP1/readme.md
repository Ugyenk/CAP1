# Dzongkha Spelling Checker

## Project Overview
This project provides a tool to check the spelling of Dzongkha text using a custom dictionary of Dzongkha words. It cleans up and processes Dzongkha words, identifies spelling errors, and provides a way to maintain an accurate dictionary.

## Table of Contents
- [Usage](#usage)
- [Implementation Details](#implementation-details)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [References](#references)

## Usage
Clean the Dictionary:

Create a text file named dictionary1.txt with your Dzongkha words.

Run clean_dzongkha_dictionary.py to clean the dictionary:

python clean_dzongkha_dictionary.py
This will generate cleaned_dictionary.txt.

Convert DOCX to TXT (if needed):

If you have a DOCX file (337.docx) that needs to be cleaned and converted, run:

python clean_docx.py

Spell Check:

Create an input_text.txt file with the text you want to check.

Run dzongkha_spelling_checker.py to check for spelling errors:

python dzongkha_spelling_checker.py

'''bash
python dzongkha_spell_checker.py input_file.txt
'''

## Implementation Details
Importing Modules
re: Used for regular expressions to identify patterns in text.
Functions

load_dzongkha_dictionary(file_path): Reads the dictionary file and loads Dzongkha words into a set for fast lookup.
   def load_dzongkha_dictionary(file_path):
       with open(file_path, 'r', encoding='utf-8') as file:
           return set(word.strip() for word in file.readlines())

is_correct_word(word, dictionary): Checks if a word is present in the loaded dictionary.
   def is_correct_word(word, dictionary):
       return word in dictionary

spell_check(text, dictionary): Processes the input text, extracts words, and checks each against the dictionary to identify misspelled words.
  def spell_check(text, dictionary):
      words = re.findall(r'\b\w+\b', text)
      errors = [word for word in words if not is_correct_word(word,  dictionary)]
      return errors

Main Logic
Load the Dictionary: Uses load_dzongkha_dictionary to load words from cleaned_dictionary.txt.
    dzongkha_dictionary = load_dzongkha_dictionary('cleaned_dictionary.txt')

Read Input Text: Reads text from input_text.txt
   with open('input_text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

Spell Check: Calls spell_check to find spelling errors in the input text.
     errors = spell_check(input_text, dzongkha_dictionary)

if errors:
    print("Spelling errors:", errors)
else:
    print("No spelling errors")
## Output
Error Reporting: Prints out misspelled words or confirms if there are no errors.

## Data Structures
Set:

Purpose: Stores dictionary words.

Reason: Fast look-up (O(1) complexity).

Example:dzongkha_dictionary = load_dzongkha_dictionary('cleaned_dictionary.txt')

List:

Purpose: Holds lines from the file and cleaned words.

Reason: Dynamic storage, easy to process.

Example:cleaned_words = [word.strip() for word in lines if is_dzongkha_word(word.strip())]

String Manipulation:

Purpose: Clean and process text.

Reason: Extract relevant words.

Example:words = re.findall(r'\b\w+\b', text)

## Algorithims
Load Dictionary:

Reads words from a file and puts them in a set for quick access.

Code:def load_dzongkha_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file.readlines())
Check Word:

Checks if a word is in the dictionary.

Code:def is_correct_word(word, dictionary):
    return word in dictionary
Spell Check:

Finds all words in text and checks each against the dictionary.

Code:def spell_check(text, dictionary):
    words = re.findall(r'\b\w+\b', text)
    errors = [word for word in words if not is_correct_word(word, dictionary)]
    return errors

## Performence analysis
Dictionary Loading:

Time: Efficient for small to medium-sized dictionaries.
Memory: Uses a set for quick look-up, keeping memory use moderate.
Spell Checking:
Time: Efficient, with O(n) complexity for text processing and O(1) for dictionary look-up.
Process: Regex finds words fast, and set look-ups confirm accuracy.
Bottlenecks and Considerations:
Large Files: May slow down initial load and increase memory use.
Regex Efficiency: Effective but can be slower with very large texts.
Overall:
Strengths: Fast, efficient, clear logic.
Weaknesses: Dependent on file size, regex complexity.

## Challenge and Solutions
Non-Dzongkha Characters:
Challenge: Filtering out non-Dzongkha words.
Solution: Used regex to match only Dzongkha characters.

Large Dictionary:
Challenge: Efficiently managing large dictionaries.
Solution: Stored words in a set for fast look-up.

## Future Improvements
Expand Dictionary:
Add more Dzongkha words to increase accuracy.

User Interface:
Develop a graphical user interface (GUI) for easier interaction.

Real-time Spell Checking:
Implement real-time spell checking as users type.

Performance Optimization:
Optimize algorithms for faster processing of large files.

Language Support:
Extend support to other languages using a similar framework.

## Refferences

1.[Python re Module Documentation](https://docs.python.org/3/library/re.html?form=MG0AV3)
2.[Python set Data Structure](https://docs.python.org/3/tutorial/datastructures.html?form=MG0AV3#sets)
3.[python-docx Documentation](https://python-docx.readthedocs.io/en/latest/?form=MG0AV3)
4.[Unicode character database](https://www.unicode.org/ucd/?form=MG0AV3)