#
# Discrete logarithm zero knoledge protocol definition
#
import random

class dlog:
    def __init__(self, module, generator):
        self.param = {"module" : module, "generator" : generator, "n_chall" : 2}
        self.target = 0
        self.round = -1
        self.setups = []
        self.challenge_bits = []
        self.resps = []

    def nextRound(self):
        self.round += 1

    def getModule(self):
        return self.param["module"]
    
    def getGen(self):
        return self.param["generator"]
    
    def getN_chall(self):
        return self.param["n_chall"]
    
    def getRound(self):
        return self.round
    
    class Prover:
        def __init__(self, secret):
            self.secret = secret
            self.setup_data = []

    def proverSetup(self, prover):
        if self.target == 0:
            self.target = pow(self.getGen(), prover.secret, self.getModule())
        self.nextRound()
        p = self.getModule()
        r = random.randint(0,p-1)
        g = self.getGen()
        C = pow(g,r,p)
        prover.setup_data.append([r, C])
        self.setups.append(C)
        
    
    def proverResp(self, prover):
        round = self.round
        bit = self.challenge_bits[round]
        r = prover.setup_data[round][0]
        if bit == 0:
            # sends g^r
            self.resps.append(r)
        elif bit == 1:
            # sends x+r mod p-1
            p = self.getModule()
            self.resps.append( (prover.secret + r) % (p-1) )
        else:
            assert False, "Error challenge bit"

    class Verifier:
        def __init__(self):
            return None

    def verifierChall(self, verifier):
        challenge_bit = random.randint(0,self.getN_chall() - 1)
        self.challenge_bits.append(challenge_bit)
        return challenge_bit
    
    def verifierOutput(self, verifier):
        round = self.round
        bit = self.challenge_bits[round]
        C = self.setups[round]
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