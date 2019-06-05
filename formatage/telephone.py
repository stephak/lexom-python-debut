class Telephone:
    mobile = ''
    mobile_normalise=''
    adr2 = ''
    adr3 = ''
    cp = ''
    ville = ""

    def __init__(self, mobile=''):
        self.mobile = mobile
        self.mobile_normalise=self.normalise()

    def normalise(self):
        t=''
        for elt in self.mobile:
            if elt in ['0','1','2','3','4','5','6','7','8','9']:
                t+=elt
        return t


    def print(self):
        if len(self.mobile) > 0:
            print("mobile=",self.mobile)
            print("mobile normalisé=", self.mobile_normalise)



#a = Telephone(mobile="06859   624 ¨87")
#a.print()