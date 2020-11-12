#
# Square zero knoledge protocol definition
#
import random

class square:
    def __init__(self, module, generator):
        self.param = {"module" : module, "n_chall" : 2}
        self.target = 0
        self.round = -1
        self.setups = []
        self.challenge_bits = []
        self.resps = []

    def nextRound(self):
        self.round += 1

    def getModule(self):
        return self.param["module"]
    
    def getN_chall(self):
        return self.param["n_chall"]
    
    def getRound(self):
        return self.round
    
    class Prover:
        def __init__(self, secret):
            self.secret = secret
            self.setup_data = []

    def proverSetup(self, prover):
        p = self.getModule()
        if self.target == 0:
            self.target = (prover.secret**2)%p
        self.nextRound()        
        r = random.randint(0,p-1)
        a = (r**2) % p
        prover.setup_data.append([r, a])
        self.setups.append(a)
        
    
    def proverResp(self, prover):
        round = self.round
        bit = self.challenge_bits[round]
        r = prover.setup_data[round][0]
        if bit == 0:
            # sends r
            self.resps.append(r)
        elif bit == 1:
            # sends r*secret
            p = self.getModule()
            self.resps.append( (prover.secret*r) % p )
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
        a = self.setups[round]
        p = self.getModule()
        if bit == 0:
            # checks r^2 == a
            r = self.resps[round]
            out = (r**2) % p == a
            return out
        elif bit == 1:
            # checks (r*secret)^2 == a*y
            root = self.resps[round]
            y = self.target
            out = (root**2) % p == (a*y) % p
            return out
        else:
            assert False, "Error challenge bit"