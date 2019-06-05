#f25-fuzzy.py
from fuzzywuzzy import fuzz #là on peut l'importer, et on ne va utiliser que la méthode fuzz
print(fuzz.ratio("1 rue des Oiseaux", "rue oiseaux"))
print(fuzz.ratio("1 rue des Oiseaux", "rue zOiselle"))