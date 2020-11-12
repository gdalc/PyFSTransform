#
# This is the file containing functions of the zero knowledge protocol
#

import random

##
## p_name: string encoding the ZK protocol chosen
## param: parameters of the protocol eg. base field, number of challenges
##
class Protocol:
    def __init__(self, p_name, param):
        from protocols.p_name import *
        self.protocol = p_name(param)
    
    def prover_setup(self):
    return setup

def verifier_chall(protocol, param, setup):
    # TODO
    challenge_bit = random.getrandbits()
    return challenge_bit

def prover_resp(protocol):
    # TODO
    response = 0
    return response

def verifier_output(protocol):
    return 