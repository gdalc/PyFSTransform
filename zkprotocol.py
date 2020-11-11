#
# This is the file containing functions of the zero knowledge protocol
#

import random

##
## protocol: string encoding the ZK protocol chosen
## param: parameters of the protocol eg. base field, number of challenges
def prover_setup(protocol, param):
    # TODO
    setup = 0
    return setup

def verifier_chall(protocol, param, setup):
    # TODO
    challenge_bit = random.getrandbits()
    return challenge_bit

def prover_resp(protocol, param, setup, challenge_bit):
    # TODO
    response = 0
    return response

def verifier_output(protocol, param, setup, challenge_bit, response):
    # TODO
    accept = 0
    return accept