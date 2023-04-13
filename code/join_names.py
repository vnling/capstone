import pandas as pd

authors = pd.read_csv('test_authors.txt', sep='\t', names=['AuthorId', 'Rank', 'NormalizedName', 'DisplayName', 'LastKnownAffiliationId', 'PaperCount', 'CitationCount', 'Unknown', 'CreateDate'])
editors = pd.read_csv('../mag_data/aer.aggregate.cleaned.txt', names=['Name'])

found = editors.join(authors.set_index('DisplayName'), on='Name', how='left')
found.to_csv('aer_matched.csv')