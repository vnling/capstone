import pandas as pd

papers = pd.read_csv('./eco_published.txt', sep='\t', names=['PaperId','PaperRank', 'Doi','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','OnlineDate','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId', 'Volume','Issue','FirstPage','LastPage','ReferenceCount','PaperCitationCount','EstimatedCitation','OriginalVenue','FamilyId','FamilyRank', 'N/A','CreatedDate'])
affiliations = pd.read_csv('./PaperAuthorAffiliations.txt', sep='\t', names=['PaperId','AuthorId', 'AffiliationId', 'AuthorSequenceNumber', 'OriginalAuthor', 'OriginalAffiliation'])
authors = pd.read_csv('./Authors.txt', sep='\t', names=['AuthorId', 'Rank', 'NormalizedName', 'DisplayName', 'LastKnownAffiliationId', 'PaperCount', 'AuthorCitationCount', 'Unknown', 'CreateDate'])

paper_affiliations = papers.join(affiliations.set_index('PaperId'), on=['PaperId'], how='left')
paper_authors = paper_affiliations.join(authors.set_index('AuthorId'), on=['AuthorId'], how='left')

paper_authors.to_csv('./eco_authors.csv')