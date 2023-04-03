"""
if line contains "editor" (case agnostic):
    then set "role" to contents of entire line

"""

import sys

def preprocess_no_affiliation(input, output):
    role = 'none'
    name = 'none'
    result = open(output, 'w')
    with open(input, 'r') as text:
        for line in text:
            if line.strip() == "":
                continue
            if 'editor' in line.lower():
                role = line.title()
            else:
                name = line.title().rstrip()
                result.write(name + ',' + role)
    result.close()

def preprocess_affiliation(input, output):
    role = 'none'
    name = 'none'
    affiliation = ''
    result = open(output, 'w')
    with open(input, 'r') as text:
        for line in text:
            if line.strip() == "":
                continue
            if 'editor' in line.lower() or 'manager' in line.lower():
                role = line.title().rstrip()
                continue
            if len(line.split(',', 1)) <= 1:
                name = line.title().rstrip()
                affiliation = ''
            else:
                name, affiliation = line.split(',', 1)
                name = name.title().rstrip()
                affiliation = affiliation.strip()
            result.write(name + ',' + role + ',' + affiliation + '\n')
    result.close()

def main():
    args = sys.argv[1:]
    preprocess_affiliation(args[0], args[1])

main()