import csv
from googletrans import Translator

headers = ['Preferred Label', 'Synonyms', 'Definitions', 'Obsolete', 'CUI', 'Semantic Types', 'Parents', 'Preferred Label pt', 'Synonyms pt', 'Definitions pt', 'Obsolete pt', 'CUI pt', 'Semantic Types pt', 'Parents pt']
translator = Translator()

def translate_row(row):
    ''' Translate elements A and B within `row`. '''
    origins, translations = [], []
    print(row)
    for elem in row:
    	if elem.strip() == '':
    		origins.append('')
    		translations.append('')
    	else:
	    	a = translator.translate(str(elem), src='en', dest='pt')
	    	origins.append(a.origin)
	    	translations.append(a.text)
    return origins + translations

if __name__ == '__main__':
	translations = []
	with open('data.csv') as f:
		reader = csv.reader(f, delimiter=',', quotechar='|')
		for row in reader:
			translations.append(translate_row(row))

	with open('translations.csv', 'w') as f:
		writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(headers)
		for row in translations:
			writer.writerow(row)