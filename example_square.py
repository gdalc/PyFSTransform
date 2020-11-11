from square import *
import random

p = 2**127 + 45
g = random.randint(1,p - 1)
zkp = square(p, g)

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