#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json
import ecdsa
import codecs
import pymongo

from .key import Key
from .storage import *
from .block import *
from .payload import *
from ..utilities.utilities import *


server_sk_string = 'a31fc297be78f5eb37d3d87f3194d3fd241a647b9025b59de1c61b566113d428'
server_sk = ecdsa.SigningKey.from_string(codecs.decode(server_sk_string, 'hex'), curve=ecdsa.SECP256k1)
server_vk=server_sk.get_verifying_key()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blockchain"]

class Blockchain:


    def __init__(self, block):
        self.__key = Key()
        self.__storage = StorageDatabase()
        self.__height = 0
        assert block.get == 0
        self.blocks.insert_one(block.dict())
        self.height = 0
        self.lasthash = block.hash()
        assert block['_id'] == 0
        self.blocks.insert_one(block.dict())

    def is_valid(self):
        pass

    def add_block(self, Block):
        pass

    def get_block_by_height(self, height):
        pass

    def get_block_by_hash(self, hash):
        pass

    def create_genesis_payload(self):
        genesis_payload = Payload()
        genesis_payload.set_data('Talk is cheap')
        #print(to_base58(sk.to_string()))
        user_sk_string ='2YPag2K7smFqMaU7mwmMpprHP5YuM1wWxtEv25bufuQWmjz5Zj'
        user_vk_string ='YRkLJ69vmAg8619JfcLD786CCAJ7APZueiDAdgaXwAHyToLfVfemah54VSLHPr3GVNn1KwUMb6Lm4QPtu5b8zMpMeAVi'
        user_vk_byte = from_base58(user_vk_string)
        user_vk = ecdsa.VerifyingKey.from_string(user_vk_byte, curve=ecdsa.SECP256k1)
        user_sk_byte= from_base58(user_sk_string)
        user_sk= ecdsa.SigningKey.from_string(user_sk_byte, curve=ecdsa.SECP256k1)
        genesis_payload.set_public_key(user_vk)
        signature=get_signature(get_data_hash(genesis_payload.get_data()),user_sk)
        genesis_payload.set_signature(signature)
        assert genesis_payload.is_valid()
        return genesis_payload

    def create_genesis_block(self):
        genesis_block = Block()
        genesis_block.set_version(1)
        genesis_payload= self.create_genesis_payload()
        genesis_block.set_payload([genesis_payload,])
        genesis_block.set_prev_hash('0')
        genesis_block.set_timestamp(1537016400)
        genesis_block.set_height(1)
        genesis_block.set_signature()
        genesis_block.set_hash_value()

        '''
        block.set_version(0)
        self.assertEqual(0, block.get_version())

        block.set_payload(['D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY6', ])
        self.assertEqual(['D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY6', ], block.get_payload())

        block.set_prev_hash('GKud7tATKAtSkfVEeLA9PHcTMeJ9K51Uv')
        self.assertEqual('GKud7tATKAtSkfVEeLA9PHcTMeJ9K51Uv', block.get_prev_hash())

        block.set_timestamp(12345678)
        self.assertEqual(12345678, block.get_timestamp())

        block.set_signature('D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY8')
        self.assertEqual('D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY8', block.get_signature())

        block.set_height(10)
        self.assertEqual(10, block.get_height())

        block.set_hash_value()
        print(block.get_hash_value())
        self.assertNotEqual('', block.get_hash_value())
        '''