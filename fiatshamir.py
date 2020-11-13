from protocols.dlog import *
from protocols.square import *

import hashlib

class Signature:
    def __init__(self, protocol, security=128, hash=hashlib.sha256):
        self.protocol = protocol
        self.security = security
        self.hash = hash
        self.sk = protocol.prover.secret
        self.pk = protocol.param
        return None

    def setChallengeBits(self, document, cmt):
        digest = self.hash(document.encode() + str(cmt).encode()).hexdigest()[0:32]
        challenge_bits = '{0:0128b}'.format(int(digest,16))
        return [int(x) for x in challenge_bits]

    def sign(self, document):
        for i in range(self.security):
            self.protocol.proverSetup()
        cmt = self.protocol.setups
        self.protocol.challenge_bits = self.setChallengeBits(document, cmt)
        self.protocol.round = 0
        for i in range(self.security):
            self.protocol.proverResp()
            self.protocol.nextRound()
        return [self.protocol.setups, self.protocol.resps]
    
    def verify(self, document, signature):
        cmt = signature[0]
        resps = signature[1]
        bits = self.setChallengeBits(document, cmt)
        if bits != self.protocol.challenge_bits:
            return 0
        self.protocol.round = 0
        for i in range(self.security):
            current_cmt = cmt[self.protocol.round]
            current_bit = bits[self.protocol.round]
            if False == self.protocol.verifierOutput(current_bit, current_cmt):
                return False
            self.protocol.nextRound()
        return True

if __name__ == '__main__':
    zkp = square() #or set zkp = dlog()
    zkp.setSecret()
    FST = Signature(zkp)
    document = "0123456789"
    signature = FST.sign(document)
    print(FST.verify(document, signature))