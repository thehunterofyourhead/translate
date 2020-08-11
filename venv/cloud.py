# Importa pandas library for inmporting CSV
import pandas as pd

# Imports the Google Cloud client library
from googletrans import Translator

# Instantiates a client
translate_client = Translator()


# Translating the text to specified target language
def translate(word):
    # Target language
    target_language = 'pt'  # Add here the target language that you want to translate to
    # Translates some text into Russian
    translation = translate_client.translate(
        word,
        target_language=target_language)

    return (translate_client['translatedText'])


# Import data from CSV
def importCSV():
    data = pd.read_csv('data.csv')
    countRows = (len(data))

    # Create a dictionary with translated words
    translatedCSV = {"Class": [], "ID": [], "Preferred": [], "Label": [], "Synonyms": [], "Definitions": [], "Obsolete": [], "CUI": [], "Semantic": [], "Types": [], "Parents": [], "database_cross_reference": [], "definition": [], "has_alternative_id": [], "has_exact_synonym": [], "has_obo_format_version": [], "has_obo_namespace": [], "has_related_synonym": [], "http://data.bioontology.org/metadata/prefixIRI": [], "http://purl.org/dc/elements/1.1/description": [], "http://purl.org/dc/elements/1.1/title": [], "http://purl.org/dc/terms/license": [], "http://www.geneontology.org/formats/oboInOwl#auto-generated-by": [], "http://www.geneontology.org/formats/oboInOwl#creation_date": [], "http://www.geneontology.org/formats/oboInOwl#default-namespace": [], "http://www.geneontology.org/formats/oboInOwl#id": [], "http://www.geneontology.org/formats/oboInOwl#saved-by": [], "http://www.w3.org/2000/01/rdf-schema#comment": [], "http://www.w3.org/2000/01/rdf-schema#label": [], "http://www.w3.org/2002/07/owl#deprecated": [], "http://www.w3.org/2004/02/skos/core#notation": [], "part_of": []}  # Change the column names accordingly to your coumns names

    # Translated word one by one from the CSV file and save them to the dictionary
    for index, row in data.iterrows():
        translatedCSV['Class'].append(translate(row['Class']))
        translatedCSV["ID"].append(translate(row['ID']))
        translatedCSV["Preferred"].append(translate(row["Preferred"]))
        translatedCSV["Label"].append(translate(row["Label"]))
        translatedCSV["Synonyms"].append(translate(row["Synonyms"]))
        translatedCSV["Definitions"].append(translate(row["Definitions"]))
        translatedCSV["Obsolete"].append(translate(row["Obsolete"]))
        translatedCSV["CUI"].append(translate(row["CUI"]))
        translatedCSV["Semantic"].append(translate(row["Semantic"]))
        translatedCSV["Types"].append(translate(row["Types"]))
        translatedCSV["Parents"].append(translate(row["Parents"]))
        translatedCSV["database_cross_reference"].append(translate(row["database_cross_reference"]))
        translatedCSV["definition"].append(translate(row["definition"]))
        translatedCSV["has_alternative_id"].append(translate(row["has_alternative_id"]))
        translatedCSV["has_exact_synonym"].append(translate(row["has_exact_synonym"]))
        translatedCSV["has_obo_format_version"].append(translate(row["has_obo_format_version"]))
        translatedCSV["has_obo_namespace"].append(translate(row["has_obo_namespace"]))
        translatedCSV["has_related_synonym"].append(translate(row["has_related_synonym"]))
        translatedCSV["http://data.bioontology.org/metadata/prefixIRI"].append(translate(row["http://data.bioontology.org/metadata/prefixIRI"]))
        translatedCSV["http://purl.org/dc/elements/1.1/description"].append(translate(row["http://purl.org/dc/elements/1.1/description"]))
        translatedCSV["http://purl.org/dc/elements/1.1/title"].append(translate(row["http://purl.org/dc/elements/1.1/title"]))
        translatedCSV["http://www.geneontology.org/formats/oboInOwl#auto-generated-by"].append(translate(row["http://www.geneontology.org/formats/oboInOwl#auto-generated-by"]))
        translatedCSV["http://www.geneontology.org/formats/oboInOwl#creation_date"].append(translate(row["http://www.geneontology.org/formats/oboInOwl#creation_date"]))
        translatedCSV["http://www.geneontology.org/formats/oboInOwl#date"].append(translate(row["http://www.geneontology.org/formats/oboInOwl#date"]))
        translatedCSV["http://www.geneontology.org/formats/oboInOwl#default-namespace"].append(translate(row["http://www.geneontology.org/formats/oboInOwl#default-namespace"]))
        translatedCSV["http://www.geneontology.org/formats/oboInOwl#id"].append(translate(row["http://www.geneontology.org/formats/oboInOwl#id"]))
        translatedCSV["http://www.geneontology.org/formats/oboInOwl#saved-by"].append(translate(row["http://www.geneontology.org/formats/oboInOwl#saved-by"]))
        translatedCSV["http://www.w3.org/2000/01/rdf-schema#comment"].append(translate(row["http://www.w3.org/2000/01/rdf-schema#comment"]))
        translatedCSV["http://www.w3.org/2000/01/rdf-schema#label"].append(translate(row["http://www.w3.org/2000/01/rdf-schema#label"]))
        translatedCSV["http://www.w3.org/2002/07/owl#deprecated"].append(translate(row["http://www.w3.org/2002/07/owl#deprecated"]))
        translatedCSV["http://www.w3.org/2004/02/skos/core#notation"].append(translate(row["http://www.w3.org/2004/02/skos/core#notation"]))
        translatedCSV["part_of"].append(translate(row["part_of"]))


    # Create a Dataframe from Dictionary
    # Save the DataFrame to a CSV file
    df = pd.DataFrame(data=translatedCSV)
    df.to_csv("translatedCSV.csv", sep='\t')


# Call the function
importCSV()
