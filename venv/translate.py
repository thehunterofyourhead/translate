import pandas as pd
from googletrans import Translator

headers = ['Preferred Label', 'Synonyms', 'Definitions', 'Obsolete', 'CUI', 'Semantic Types', 'Parents', 'Preferred Label pt', 'Synonyms pt', 'Definitions pt', 'Obsolete pt', 'CUI pt', 'Semantic Types pt', 'Parents pt']
data = pd.read_csv('./data.csv')
translator = Translator()
# Init empty dataframe with much rows as `data`
df = pd.DataFrame(index=range(0,len(data)), columns=headers)

def translate_row(row):
    ''' Translate elements A and B within `row`. '''
    a = translator.translate(row[0], dest='pt')
    b = translator.translate(row[1], dest='pt')
    return pd.Series([a.origin, b.origin, a.text, b.text])


for i, row in enumerate(data.values):
    # Fill empty dataframe with given serie.
    df.loc[i] = translate_row(row)

print(df)