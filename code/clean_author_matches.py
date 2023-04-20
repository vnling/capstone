import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
correct_id = sys.argv[3]

data = pd.read_csv(input_file)

def verify_journal(df, journalid):
    res = df[df['JournalId'] == int(journalid)]
    discard = df[df['JournalId'] != int(journalid)]
    print(discard)
    return res

def drop_irrelevant_cols(df):
    res = df.drop(['PaperRank', 'Doi', 'DocType', 'OriginalTitle', 'BookTitle', 'Publisher', 
             'ConferenceSeriesId', 'ConferenceInstanceId', 'Volume', 'Issue', 'FirstPage', 
             'LastPage', 'ReferenceCount', 'PaperCitationCount', 'EstimatedCitation', 
             'FamilyId', 'FamilyRank', 'N/A', 'Unknown'], axis=1)
    return res   

def main():
    correct_journal = verify_journal(data, correct_id)
    dropped = drop_irrelevant_cols(correct_journal)
    dropped.to_csv(output_file, index=False)

main()