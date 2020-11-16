#
# Discrete logarithm zero knoledge protocol definition
#
import random
from protocols.types import *

class dlog(ZKProtocol):
    # module = prime number defining the multiplicative group
    # generator = an element generating the multiplicative group of F_p
    def __init__(self, secret = None, module = 2**127 + 45, generator = 3):
        self.param = {"module" : module, "generator" : generator, "n_chall" : 2}
        self.prover = Prover(secret)
        self.verifier = Verifier()
        super().__init__("Discrete Log in F_" + str(module) + " with generator " + str(generator))

    def setSecret(self, secret = None):
        if secret == None:
            self.prover.secret = random.randint(2,self.getModule()-2)
        else:
            self.prover.secret = secret

    def getModule(self):
        return self.param["module"]
    
    def getGen(self):
        return self.param["generator"]

    def proverSetup(self):
        if self.target == 0:
            self.target = pow(self.getGen(), self.prover.secret, self.getModule())
        self.nextRound()
        p = self.getModule()
        r = random.randint(0,p-1)
        g = self.getGen()
        C = pow(g,r,p)
        self.prover.setup_data.append([r, C])
        self.commitments.append(C)
    
    def proverResp(self):
        round = self.round
        bit = self.challenge_bits[round]
        r = self.prover.setup_data[round][0]
        if bit == 0:
            # sends g^r
            self.resps.append(r)
        elif bit == 1:
            # sends x+r mod p-1
            p = self.getModule()
            self.resps.append( (self.prover.secret + r) % (p-1) )
        else:
            assert False, "Error challenge bit"

    def verifierChall(self):
        challenge_bit = random.randint(0,self.getN_chall() - 1)
        self.challenge_bits.append(challenge_bit)
        return challenge_bit
    
    def verifierOutput(self, bit = None, C = None):
        round = self.round
        if bit == None:
            bit = self.challenge_bits[round]
        if C == None:
            C = self.commitments[round]
        p = self.getModule()
        g = self.getGen()
        if bit == 0:
            # checks g^r == C
            r = self.resps[round]
            out = pow(g,r,p) == C
            return out
        elif bit == 1:
            # checks g^(x+r mod p-1) == C*y
            exp = self.resps[round]
            y = self.target
            out = pow(g,exp,p) == (C*y) % p
            return out
        else:
            assert False, "Error challenge bit"