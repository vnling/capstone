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
    year = re.findall(r'\d{4}-\d{4}', input)
    return year[0].split('-')

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


def find_mac_substring(input):
    """
    Regex to find the substring "mac" given an input string
    """
    mac = re.findall(r'mac', input)
    return mac


def main():
    # restud_preprocess("restud_raw.csv", "restud.csv")
    print(find_mac_substring("macaroni"))

main()