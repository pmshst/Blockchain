#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json
import ecdsa

class Key:
    public_key = ''
    secret_key = ''
    def __init__(self, public_key = '', secret_key = ''):
        self.public_key = public_key
        self.secret_key = secret_key

    def set_public_key(self, public_key):
        self.public_key = public_key

    def set_secret_key(self, secret_key):
        self.secret_key = secret_key

    def get_public_key(self):
        return self.public_key

    def get_secret_key(self):
        return self.public_key

    def set_key_pairs_by_generate(self):
        self.secret_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.secret_key.get_verifying_key()
