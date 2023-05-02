import pandas as pd

journal = "aer"
authors = pd.read_csv(f"./{journal}_author_citations.csv", 
                      usecols=['AuthorId','PaperId','Year_paper','OriginalAuthor_left','CitesFrom','Year_citation'])
editors = pd.read_csv(f"./{journal}_editor_citations.csv", 
                      usecols=['AuthorId','PaperId','Year_paper','Name','CitesFrom','Year_citation'])

authors = authors.sort_values(by=['Year_paper'])
editors = editors.sort_values(by=['Year_paper'])
authors = authors[authors['Year_paper'] >= authors['Year_citation']]
editors = editors[editors['Year_paper'] >= editors['Year_citation']]
authors['PaperCount'] = authors['AuthorId'].groupby(authors.AuthorId).transform('count')
editors['PaperCount'] = editors['AuthorId'].groupby(editors.AuthorId).transform('count')

authors.head(20)
editors.head(20)

authors = authors.drop_duplicates(subset=['AuthorId'], keep='last')
editors = editors.drop_duplicates(subset=['AuthorId'], keep='last')

authors.to_csv('{journal}_authors_citations_final.csv')
editors.to_csv('{journal}_editors_citations_final.csv')