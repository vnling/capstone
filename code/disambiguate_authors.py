"""
- Filter out all names with only one paper
this is because of MAG's tendency to under-conflate, and because editors tend to be accomplished scientists
"""

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
dataframe = pd.read_csv(input_file, sep=',')

def filter_single_paper(df):
    res = df[df['PaperCount'] > 1]
    return res

def drop_duplicates(df):
    res = df.drop_duplicates(subset=['Name'], keep=False)
    return res

def random_sample_duplicates(df):
    res = df.sample(frac=1).drop_duplicates(subset=['Name']).reset_index(drop=True).sort_values(by=['Unnamed: 0'])
    return res


def main():
    multiple_papers = filter_single_paper(dataframe)
    random_duplicates = random_sample_duplicates(multiple_papers)
    random_duplicates.to_csv(output_file, index=False)

main()