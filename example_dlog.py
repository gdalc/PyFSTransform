from protocols.dlog import *
import random

# zero knowledge protocol
zkp = dlog()
p = zkp.getModule()

secret = random.randint(2,p-2)
Alice = zkp.Prover(secret)
Bob = zkp.Verifier()
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