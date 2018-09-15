#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json
import ecdsa
import codecs
from ..utilities.utilities import *

class Payload:
    data = []
    signature = ''
    public_key = ''
    def __init__(self, data = [], signature = '',  public_key = ''):
        self.data = data
        self.signature = signature
        self.public_key = public_key

    def set_data(self, data):
        self.data = data

    def set_signature(self, signature):
        self.signature = signature

    def set_public_key(self, public_key):
        self.public_key = public_key

    def get_data(self):
        return self.data

    def get_signature(self):
        return self.signature

    def get_public_key(self):
        return self.public_key

    def is_valid(self):
        return self.public_key.verify(from_base58(self.signature), codecs.decode(get_data_hash(self.data), 'hex'))
