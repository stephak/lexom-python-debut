class Adresse:
      adr1=''
      adr2=''
      adr3=''
      cp=''
      ville=""
      def __init__(self,adr1="",adr2="",adr3="",cp="",ville=""):
            self.adr1=adr1
            self.adr2=adr2
            self.adr3=adr3
            self.cp=cp
            self.ville=ville

      def print(self):
            if len(self.adr1)>0 : print(self.adr1)
            if len(self.adr2)>0 : print(self.adr2)
            if len(self.adr3)>0 : print(self.adr3)
            if len(self.cp+' '+self.ville)>1 : print((self.cp+' '+(self.ville)).upper())




	
#a=Adresse("8 square Louis Massignon",cp="35000",ville="Rennes")
#a.print()