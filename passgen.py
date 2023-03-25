import string
from random import randint, shuffle, choice
from hashlib import sha1,sha256

class PasswordGenerator():

    finalpass = ""
    def __init__(self, schar = "", passlen = 8, flagn = True):
        
        self.pass_len = passlen
        self.schar = list(schar)
        self._allchar = string.ascii_lowercase + string.ascii_uppercase + schar
        if flagn:
            self._allchar = list(string.digits) + list(self._allchar)

    def generate(self):
        
        final_pass = [
            choice(self.schar)
            for i in range(2)
        ]
        final_pass += [
            choice(self._allchar)
            for i in range(self.pass_len-2)
        ]

        shuffle(final_pass)
        final_pass =  "".join(final_pass)
        self.finalpass = final_pass

    def hashedpass(self,c = finalpass):
        
        if(self.finalpass): c = self.finalpass
        
        hash1 = sha1(c.encode()).hexdigest()
        hash256 = sha256(c.encode()).hexdigest()

        return hash1,hash256



