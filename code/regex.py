import re

# def aer_jpe_preprocess(raw_filepath, output_filepath):
#     """
#     Split each line in a comma separated value file named "aer_raw.csv"" into a list
#     Write the first two values of each list to a new file named "aer.csv"
#     """
#     with open(raw_filepath, 'r') as f:
#         with open(output_filepath, 'w') as f2:
#             for line in f:
#                 line = line.split(', ')
#                 f2.write(line[0] + ',,,' + line[1] + '\n')

# def restud_preprocess(raw_filepath, output_filepath):
#     with open(raw_filepath, 'r', encoding="utf8") as f:
#         with open(output_filepath, 'w', encoding="utf8") as f2:
#             for line in f:
#                 line = line.split(', ', 1) #only split once because of restud dual affiliation lists
#                 f2.write(line[0] + ',,,' + line[1])

# def aer_regex(input_filepath, output_filepath):
#     """
#     Regex to extract names and years from an input file
#     """
#     with open(input_filepath, 'r', encoding="utf8") as f:
#         with open(output_filepath, 'w', encoding="utf8") as f2:
#             for line in f:
#                 name = get_name(line)
#                 for n in name:
#                     f2.write(n + '\n')

def name_regex(text):
    name_regex = r'\s*(?:[A-Z][a-z]*\-?[A-Z]?[a-z]*\.?(?:\s+[A-Z][a-z]*\-?[A-Z]?[a-z]*\.?)?)\s+[A-Z][a-z]*\-?[A-Z]?[a-z]*\.?\b'
    names = re.findall(name_regex, text)
    return list(set(names))

def institution_regex(text):
    # university_regex = r'\b[A-Z][a-z]*\s*(?:[A-Z][a-z]*\s*)+(?:College|University)\b'
    university_regex = r'\b(?:[A-Z][a-z]*\s*)+(?:College|University)(?:(?:\s+(?:of|at)\s+)|(?:\s+))(?:[A-Z][a-z]*\s*)+\b'
    institutions = re.findall(university_regex, text)
    return list(set(names))

def main():
    test = "John Smith andMary Johnson went to the store. They met up with Susan Brown. He asked if it was okay to add T. Tim to the guest list. Also, he mentioned that his friend Robert E. Lee would be joining us. Last but not least, we cannot forget about Anna-Marie Martinez and Carlos García-Sánchez."
    names = name_regex(test)
    print(names)

main()