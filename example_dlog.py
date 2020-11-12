from protocols.dlog import *
import random

# zero knowledge protocol
zkp = dlog()
Alice = zkp.prover
zkp.setSecret()
Bob = zkp.verifier
result = []
for i in range(4):
    # 1
    zkp.proverSetup(Alice)
    # 2
    zkp.verifierChall(Bob)
    # 3
    zkp.proverResp(Alice)
    # 4
    result.append(zkp.verifierOutput(Bob))

print("Challenges: ", zkp.challenge_bits)
print("Results: ", result)