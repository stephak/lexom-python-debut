import sys
#si ailleurs sys.path.append('/Users/stephanehakni/dev/mesmodules/')

from formatage import adresse
from formatage import telephone



a=adresse.Adresse("8 square Louis Massignon",cp="35000",ville="Rennes")
a.print()

tel = telephone.Telephone(mobile="06859   624 ¨87")
tel.print()

