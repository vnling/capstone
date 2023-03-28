import re
import sys
from sortedcollections import OrderedSet

"""
try feeding chatgpt desired input + output (one shot learning)
- ineffective, chatgpt instead would summarize the text

extract page with editor names
- done for aer
"""

def name_regex(text):
    # overcomplicated name_regex = r'\s*(?:[A-Z][a-z]*\-?[A-Z]?[a-z]*\.?(?:\s+[A-Z][a-z]*\-?[A-Z]?[a-z]*\.?)?)\s+[A-Z][a-z]*\-?[A-Z]?[a-z]*\.?\b'
    simple_name_regex = r"\b[A-ZÀ-ÿ][a-zÀ-ÿ]* [A-ZÀ-ÿ][A-ZÀ-ÿa-z'-.]*"
    names = re.findall(simple_name_regex, text)
    return list(OrderedSet(names))

# search "editor", then grab everything after that until next "editor"
def aer_editor_regex(text):
    first_block = r'Editor.*ECONOMIC\n\nREVIEW'
    # second_block = r'Board of Editors.*Editorial Offices'
    first_editors = re.findall(first_block, text, re.DOTALL)
    # second_editors = re.findall(second_block, text, re.DOTALL)
    return first_editors #+ second_editors

def institution_regex(text):
    # university_regex = r'\b[A-Z][a-z]*\s*(?:[A-Z][a-z]*\s*)+(?:College|University)\b'
    university_regex = r'\b(?:[A-Z][a-z]*\s*)+(?:College|University)(?:(?:\s+(?:of|at)\s+)|(?:\s+))(?:[A-Z][a-z]*\s*)+\b'
    institutions = re.findall(university_regex, text)
    return list(set(institutions))

def main():
    args = sys.argv[1:]
    textfile = open(args[0], 'r')
    result = open(args[1], 'w')
    text = textfile.read()
    names = aer_editor_regex(text)
    print(names)
    result.write('\n'.join(names))
    textfile.close()
    result.close()

main()