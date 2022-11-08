import re

def get_name(input):
    """
    Regex to extract name from an input string
    """
    name = re.findall(r'^[A-Z][a-z]+ [A-Z][a-z]+', input)
    return name

def get_year(input):
    """
    Regex to extract start and end year from an input string with year format YYYY-YYYY
    """
    year = re.findall(r'\d{4}', input)
    return year

def aer_jpe_preprocess(raw_filepath, output_filepath):
    """
    Split each line in a comma separated value file named "aer_raw.csv"" into a list
    Write the first two values of each list to a new file named "aer.csv"
    """
    with open(raw_filepath, 'r') as f:
        with open(output_filepath, 'w') as f2:
            for line in f:
                line = line.split(', ')
                f2.write(line[0] + ',,,' + line[1] + '\n')

def restud_preprocess(raw_filepath, output_filepath):
    with open(raw_filepath, 'r', encoding="utf8") as f:
        with open(output_filepath, 'w', encoding="utf8") as f2:
            for line in f:
                line = line.split(', ', 1) #only split once because of restud dual affiliation lists
                f2.write(line[0] + ',,,' + line[1])

"""
make sure affiliations do not have commas
or affiliations will be split into multiple columns

keep national affiliation with institution 

double check the UCs
"""

def aer_regex(input_filepath, output_filepath):
    """
    Regex to extract names and years from an input file
    """
    with open(input_filepath, 'r', encoding="utf8") as f:
        with open(output_filepath, 'w', encoding="utf8") as f2:
            for line in f:
                name = get_name(line)
                year = get_year(line)
                print(name, year)
                # f2.write(name[0] + ',' + year[0] + '\n')


def main():
    # restud_preprocess("restud_raw.csv", "restud.csv")
    aer_regex("./../pdf/10.1257_aer.112.1.i.txt", "./../pdf/processed_10.1257_aer.112.1.i.txt")

main()