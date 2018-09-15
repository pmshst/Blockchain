#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json

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

    def __init__(self, version  = 0, payload = [], prev_hash = '', timestamp = 0, signature = '', hash_value = '', height =0):
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

    def set_signature(self, signature):
        self.__signature = signature

    def set_hash_value(self):
        payload_str ="".join(self.__payload)
        block_string = self.__prev_hash.encode('utf-8') + str(self.__timestamp).encode('utf-8') + str(self.__height).encode('utf-8') + \
                       str(self.__version).encode('utf-8') + payload_str.encode('utf-8') + self.__signature.encode('utf-8')

        self.__hash_value = hashlib.sha256(block_string).hexdigest()

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

