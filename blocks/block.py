#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json

class Block:
    version = 0
    payload = []
    prev_hash = ''
    timestamp = int(time.time())
    signature = ''
    hash_value = ''
    height=0



    def __init__(self, version  = 0, payload = [], prev_hash = '', timestamp = 0, signature = '', hash_value = '', height =0):
        self.version = version
        self.payload = payload    #payload store data
        self.prev_hash = prev_hash
        self.timestamp =timestamp
        self.signature = signature
        self.hash_value = hash_value
        self.height = height

    def set_version(self, version):

        self.version = version

    def set_payload(self, payload):
        self.payload = payload

    def set_prev_hash(self, prev_hash):
        self.prev_hash = prev_hash

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def set_signature(self, signature):
        self.signature = signature

    def set_hash_value(self):
        payload_str ="".join(self.payload)
        block_string = self.prev_hash.encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.height).encode('utf-8')+ \
                       str(self.version).encode('utf-8') + payload_str.encode('utf-8') + self.signature.encode('utf-8')

        self.hash_value = hashlib.sha256(block_string).hexdigest()

    def set_height(self, height):
        self.height = height

    def get_version(self):
        return self.version

    def get_payload(self):
        return self.payload

    def get_prev_hash(self):
        return self.prev_hash

    def get_timestamp(self):
        return self.timestamp

    def get_signature(self):
        return self.signature

    def get_hash_value(self):
        return self.hash_value

    def get_height(self):
        return self.height

