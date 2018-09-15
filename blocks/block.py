#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json
import ecdsa
from ..utilities.utilities import *
from .payload import Payload

serversk_string = 'a31fc297be78f5eb37d3d87f3194d3fd241a647b9025b59de1c61b566113d428'
serversk = ecdsa.SigningKey.from_string(codecs.decode(serversk_string, 'hex'), curve=ecdsa.SECP256k1)

servervk_string = '27a505f67abd3f61882d7840af25346661fe96582af181351cb2e088d2d2c909ffdbc406be350da657974df0fc3dcbc47' \
                  'cb0ecccc459aed41269dd7b39f6dc59'

servervk = ecdsa.VerifyingKey.from_string(codecs.decode(servervk_string, 'hex'), curve=ecdsa.SECP256k1)


class Block:
    '''
    __version = 0
    payload = []
    prev_hash = ''
    timestamp = int(time.time())
    signature = ''
    hash_value = ''
    height=0

    '''

    def __init__(self, version  = 0, payload = [Payload(),], prev_hash = '', timestamp = 0, signature = '', hash_value = '', height =0):
        self.__version = version
        self.__payload = payload    #payload store data
        self.__prev_hash = prev_hash
        self.__timestamp =timestamp
        self.__signature = signature
        self.__hash_value = hash_value
        self.__height = height

    def set_version(self, version):

        self.__version = version

    def set_payload(self, payload):
        self.__payload = payload

    def set_prev_hash(self, prev_hash):
        self.__prev_hash = prev_hash

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp
    def get_signature_string(self):
        payload_string = "".join(self.get_payload())
        signature_string = self.__prev_hash + str(self.get_timestamp()) + str(self.get_height()) + \
                           str(self.get_version()) + payload_string
        return signature_string

    def get_hash_value_string(self):

        return self.get_signature() + self.get_signature_string()

    def set_signature(self):

        self.__signature = get_signature(self.get_signature_string(),serversk)

    def set_hash_value(self):


        self.__hash_value = get_data_hash(str(self.get_hash_value_string()))

    def set_height(self, height):
        self.__height = height

    def get_version(self):
        return self.__version

    def get_payload(self):
        return self.__payload

    def get_prev_hash(self):
        return self.__prev_hash

    def get_timestamp(self):
        return self.__timestamp

    def get_signature(self):
        return self.__signature

    def get_hash_value(self):
        return self.__hash_value

    def get_height(self):
        return self.__height


