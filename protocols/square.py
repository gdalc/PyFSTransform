#
# Square zero knoledge protocol definition
#
import random
from protocols.types import *

class square(ZKProtocol):
    # module = integer defining the ring Z_n
    def __init__(self, secret = None, module = 2**127 + 45):
        self.param = {"module" : module, "n_chall" : 2}
        self.prover = Prover(secret)
        self.verifier = Verifier()
        super().__init__("Square on " + str(module))
    
    def setSecret(self, secret = None):
        if secret == None:
            self.prover.secret = random.randint(2,self.getModule()-2)
        else:
            self.prover.secret = secret

    def getModule(self):
        return self.param["module"]

    def proverSetup(self):
        n = self.getModule()
        if self.target == 0:
            self.target = ( self.prover.secret**2 ) % n
        self.nextRound()        
        r = random.randint(0,n-1)
        a = (r**2) % n
        self.prover.setup_data.append([r, a])
        self.commitments.append(a)
        
    
    def proverResp(self):
        round = self.round
        bit = self.challenge_bits[round]
        r = self.prover.setup_data[round][0]
        if bit == 0:
            # sends r
            self.resps.append(r)
        elif bit == 1:
            # sends r*secret
            n = self.getModule()
            self.resps.append( (self.prover.secret*r) % n )
        else:
            assert False, "Error challenge bit"

    def verifierChall(self):
        challenge_bit = random.randint(0,self.getN_chall() - 1)
        self.challenge_bits.append(challenge_bit)
    
    def verifierOutput(self, bit = None, a = None):
        round = self.round
        if bit == None:
            bit = self.challenge_bits[round]
        if a == None:
            a = self.commitments[round]
        n = self.getModule()
        if bit == 0:
            # checks r^2 == a
            r = self.resps[round]
            out = (r**2) % n == a
            return out
        elif bit == 1:
            # checks (r*secret)^2 == a*y
            root = self.resps[round]
            y = self.target
            out = (root**2) % n == (a*y) % n
            return out
        else:
            assert False, "Error challenge bit"