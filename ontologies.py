import rdflib
from rdflib import Namespace
from rdflib.namespace import OWL

g = rdflib.Graph()

ontologia1 = g.parse('cido.owl', format='OWL')

s = ontologia1.serialize(format='RDF').decode('utf-8')

with open('cido.rdf') as f:
    f.write(s)

