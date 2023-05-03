import pandas as pd

journal = "aer"

authors = pd.read_csv(f"./{journal}_authors_cleaned.csv", usecols=['Year', 'AuthorId']).dropna(subset=['AuthorId'])
authors = authors.astype({'AuthorId': int})
authors = authors.rename(columns={'Year': 'PaperYear'})
authors = authors.sort_values(by=['PaperYear'])
authors = authors.drop_duplicates(subset=['AuthorId'], keep='last')

editors = pd.read_csv(f"{journal}_random_duplicates.csv", usecols=['Name', 'AuthorId']).dropna(subset=['AuthorId'])
editors = editors.astype({'AuthorId': int})
tenures = pd.read_csv(f"{journal}.tenures.csv", usecols=['Name', 'End'])
editors = editors.merge(tenures, on=['Name'], how='inner')
editors = editors.rename(columns={'End': 'PaperYear'})
editors = editors.sort_values(by=['PaperYear'])
editors = editors.drop_duplicates(subset=['AuthorId'], keep='last')

author_citations = pd.read_csv(f"./{journal}_author_citations.csv", 
                      usecols=['AuthorId','PaperId','Year_paper','OriginalAuthor_left','CitesFrom','Year_citation'])
editor_citations = pd.read_csv(f"./{journal}_editor_citations.csv", 
                      usecols=['AuthorId','PaperId','Year_paper','Name','CitesFrom','Year_citation'])

authors = authors.join(author_citations.set_index('AuthorId'), on=['AuthorId'], how='left')
editors = editors.join(editor_citations.set_index('AuthorId'), on=['AuthorId'], how='left', lsuffix="_left", rsuffix="_right")

authors = authors[authors['PaperYear'] >= authors['Year_citation']]
editors = editors[editors['PaperYear'] >= editors['Year_citation']]
authors['PaperCount'] = authors['AuthorId'].groupby(authors.AuthorId).transform('count')
editors['PaperCount'] = editors['AuthorId'].groupby(editors.AuthorId).transform('count')

authors = authors.drop_duplicates(subset=['AuthorId'], keep='last')
editors = editors.drop_duplicates(subset=['AuthorId'], keep='last')

authors.to_csv(f'{journal}_authors_citations_final.csv')
editors.to_csv(f'{journal}_editors_citations_final.csv')