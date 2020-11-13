from protocols.square import *
import random

# zero knowledge protocol
zkp = square()
n = zkp.getModule()

secret = random.randint(2,n-2)
Alice = zkp.prover
zkp.setSecret()
Bob = zkp.verifier
result = []
for i in range(4):
    # 1
    zkp.proverSetup()
    # 2
    zkp.verifierChall()
    # 3
    zkp.proverResp()
    # 4
    result.append(zkp.verifierOutput())

print("Challenges: ", zkp.challenge_bits)
print("Results: ", result)