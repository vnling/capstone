import pandas as pd

"""
#### Get Paper Counts Up to Year Published
- get the paper and citation counts up until year that they published in journal
- all unique authors and editors
- for each contributor, get all their papers1
- get number of papers1 published per year/end of bin?
- line with confidence interval (look into seaborn)
"""

# reference = pd.read_csv("./../paper_references_sample.txt", sep="\t", 
#                         names = ['CitesFrom', 'BeingCited'], memory_map=True)

# def get_paper_counts(journal):

import pandas as pd

journal = "aer"

"""
first try
"""
papers = pd.read_csv("./Papers.txt", sep="\t",low_memory=False,usecols=['PaperId', 'Year'], dtype={'PaperId':'object', 'Year':'object'}, names=['PaperId','PaperRank', 'Doi','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','OnlineDate','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId', 'Volume','Issue','FirstPage','LastPage','ReferenceCount','PaperCitationCount','EstimatedCitation','OriginalVenue','FamilyId','FamilyRank', 'N/A','CreatedDate'])
print("papers loaded")
pa_affiliations = pd.read_csv('./PaperAuthorAffiliations.txt', sep='\t', low_memory=False,usecols=['PaperId', 'AuthorId', ], dtype={'PaperId':'object', 'AuthorId':'object'}, names=['PaperId','AuthorId', 'AffiliationId', 'AuthorSequenceNumber', 'OriginalAuthor', 'OriginalAffiliation'])
print("affiliations loaded")
authors = pd.read_csv(f"{journal}_authors.csv", usecols=['AuthorId', 'OriginalAuthor', 'NormalizedName', 'DisplayName'])
editors = pd.read_csv(f"{journal}_editors.csv", usecols=['Name','AuthorId','Rank','NormalizedName','LastKnownAffiliationId','PaperCount','CitationCount','Unknown','CreateDate'])

print("authors and editors loaded")

authors = authors.dropna(subset=['AuthorId'])
editors = editors.dropna(subset=['AuthorId'])
author_affiliations = authors.join(pa_affiliations.set_index('AuthorId'), on=['AuthorId'], how='inner')
author_papers = author_affiliations.join(papers.set_index('PaperId'), on=['PaperId'], how='inner')
print("authors joined")
editor_affiliations = editors.join(pa_affiliations.set_index('AuthorId'), on=['AuthorId'], how='inner')
editor_papers = editor_affiliations.join(papers.set_index('PaperId'), on=['PaperId'], how='inner')

author_papers.to_csv(f"{journal}_author_papers.csv", columns=['AuthorId', 'PaperId', 'Year', 'OriginalAuthor', 'NormalizedName', 'DisplayName'])
editor_papers.to_csv(f"{journal}_editor_papers.csv", columns=['AuthorId', 'PaperId', 'Year', 'Name', 'NormalizedName'])


"""
second try
"""
pa_affiliations = pd.read_csv('./PaperAuthorAffiliations.txt', sep='\t', names=['PaperId','AuthorId', 'AffiliationId', 'AuthorSequenceNumber', 'OriginalAuthor', 'OriginalAffiliation'])
print("affiliations loaded")
authors = pd.read_csv(f"{journal}_authors.csv", usecols=['AuthorId', 'OriginalAuthor', 'NormalizedName', 'DisplayName'])
editors = pd.read_csv(f"{journal}_editors.csv", usecols=['Name','AuthorId','Rank','NormalizedName','LastKnownAffiliationId','PaperCount','CitationCount','Unknown','CreateDate'])
print("authors and editors loaded")

authors = authors.dropna(subset=['AuthorId'])
editors = editors.dropna(subset=['AuthorId'])
author_affiliations = authors.join(pa_affiliations.set_index('AuthorId'), on=['AuthorId'], how='inner')
editor_affiliations = editors.join(pa_affiliations.set_index('AuthorId'), on=['AuthorId'], how='inner')

author_affiliations.to_csv(f"{journal}_author_intermediate.csv")
editor_affiliations.to_csv(f"{journal}_editor_intermediate.csv")

"""
second try - part two
"""
authors = pd.read_csv(f"{journal}_author_intermediate.csv")
editors = pd.read_csv(f"{journal}_editor_intermediate.csv")

papers = pd.read_csv("./Papers.txt", sep="\t", names=['PaperId','PaperRank', 'Doi','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','OnlineDate','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId', 'Volume','Issue','FirstPage','LastPage','ReferenceCount','PaperCitationCount','EstimatedCitation','OriginalVenue','FamilyId','FamilyRank', 'N/A','CreatedDate'])
print("papers loaded, joining")
author_papers = authors.join(papers.set_index('PaperId'), on=['PaperId'], how='inner', lsuffix='_left')
editor_papers = editors.join(papers.set_index('PaperId'), on=['PaperId'], how='inner', lsuffix='_left')
author_papers.to_csv(f"{journal}_author_papers.csv", columns=['AuthorId', 'PaperId', 'Year', 'OriginalAuthor_left', 'NormalizedName', 'DisplayName'])
editor_papers.to_csv(f"{journal}_editor_papers.csv", columns=['AuthorId', 'PaperId', 'Year', 'Name', 'NormalizedName'])


"""
citations - part 1
"""
reference = pd.read_csv("./PaperReferences.txt", sep="\t", names = ['CitesFrom', 'BeingCited'], memory_map=True)
author_papers = pd.read_csv(f"{journal}_author_papers.csv")
editor_papers = pd.read_csv(f"{journal}_editor_papers.csv")

reference = reference.rename(columns={'BeingCited': 'PaperId'})

author_citations = author_papers.join(reference.set_index('PaperId'), on='PaperId', how='left')
editor_citations = editor_papers.join(reference.set_index('PaperId'), on='PaperId', how='left')

author_citations.to_csv(f"{journal}_author_inter_citations.csv")
editor_citations.to_csv(f"{journal}_editor_inter_citations.csv")

"""
citations - part 2
"""
papers = pd.read_csv("./Papers.txt", sep="\t", names=['PaperId','PaperRank', 'Doi','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','OnlineDate','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId', 'Volume','Issue','FirstPage','LastPage','ReferenceCount','PaperCitationCount','EstimatedCitation','OriginalVenue','FamilyId','FamilyRank', 'N/A','CreatedDate'])
author_papers = pd.read_csv(f"{journal}_author_inter_citations.csv")
editor_papers = pd.read_csv(f"{journal}_editor_inter_citations.csv")

papers = papers.rename(columns={'PaperId': 'CitesFrom'})

author_citations = author_papers.join(papers.set_index('CitesFrom'), on='CitesFrom', how='left', lsuffix='_paper', rsuffix='_citation')
editor_citations = editor_papers.join(papers.set_index('CitesFrom'), on='CitesFrom', how='left', lsuffix='_paper', rsuffix='_citation')
author_citations = author_citations.dropna(subset=['CitesFrom'])
editor_citations = editor_citations.dropna(subset=['CitesFrom'])

author_citations.to_csv(f"{journal}_author_citations.csv", 
                        columns=['AuthorId','PaperId','Year_paper','OriginalAuthor_left','CitesFrom','Year_citation'])
editor_citations.to_csv(f"{journal}_editor_citations.csv", 
                        columns=['AuthorId','PaperId','Year_paper','Name','CitesFrom','Year_citation'])