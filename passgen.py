import string
from random import randint, shuffle, choice
from hashlib import sha1,sha256

class PasswordGenerator():

    def __init__(self, passlen = 8, flag = True):

        self.pass_len = passlen
        self._allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self._schars = [
            "!",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            ".",
            "-",
            "_",
            "@",
            "?",
        ]
        if flag:
            self._allchar = list(self._allchar) + self._schars
        else:
            pass

    def generate(self):

        final_pass = [
            choice(self._allchar)
            for i in range(self.pass_len)
        ]

        shuffle(final_pass)
        final_pass =  "".join(final_pass)
        self.finalpass = final_pass

    def hashedpass(self):
        c = self.finalpass
        hash1 = sha1(c.encode()).hexdigest()
        hash256 = sha256(c.encode()).hexdigest()

        return hash1,hash256




