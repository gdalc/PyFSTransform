class Prover:
    def __init__(self, secret = None):
        self.secret = secret
        self.setup_data = []

class Verifier:
    pass

class ZKProtocol:
    # name = name of the protocol
    def __init__(self, name):
        self.name = name
        self.round = -1
        self.target = 0
        self.commitments = []
        self.challenge_bits = []
        self.resps = []
        print("Zero-Knowledge Protocol " + name + " initialized.")

    def nextRound(self):
        self.round += 1
    
    def getRound(self):
        return self.round
    
    def setRound(self, n):
        self.round = n
    
    def getN_chall(self):
        return self.param["n_chall"]