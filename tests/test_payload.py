#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao
import unittest
import ecdsa
import base58
import codecs
from ..blocks.payload import Payload
from ..utilities.utilities import *

class TestPayload(unittest.TestCase):

    def test_is_valid(self):
        #sk = SigningKey.generate()  # uses NIST192pvk = sk.get_verifying_key()
        #signature = sk.sign("message")
        #assert vk.verify(signature, "message")

        data_string = 'message'

        data_hash=hashlib.sha256(data_string.encode('utf-8')).hexdigest()

        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()
        signature=to_base58(sk.sign(codecs.decode(data_hash, 'hex')))

        assert vk.verify(from_base58(signature), codecs.decode(data_hash, 'hex'))
        #assert vk.verify(signature, data_hash)
        payload = Payload()

        payload.set_data(data_string)
        self.assertEqual(payload.get_data(),data_string)

        payload.set_public_key(vk)
        self.assertEqual(payload.get_public_key(),vk)

        payload.set_signature(signature)
        self.assertEqual(payload.get_signature(),signature)
        self.assertEqual(payload.is_valid(),True)

