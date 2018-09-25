#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json
import ecdsa
import codecs
import pymongo

from forum.utilities.utilities import *
from forum.blocks.block import Block
from forum.blocks.key import Key
from forum.blocks.storage import *
'''
server_sk_string = 'a31fc297be78f5eb37d3d87f3194d3' \
                   'fd241a647b9025b59de1c61b566113d428'
server_sk = ecdsa.SigningKey.from_string(
    codecs.decode(server_sk_string, 'hex'),
    curve=ecdsa.SECP256k1)
server_vk = server_sk.get_verifying_key()
'''


class Blockchain:

    def __init__(self, key):
        self.__key = key
        # key_id 与 chain_id 一致
        self.__chain_id = key.id
        # one chain on storageDatabase
        self.__chain_storage = ChainStorageDatabase(self.__chain_id)
        self.__keys_storage = KeyStorageDatabase()
        self.__height = 0

    @property
    def key(self):
        """
        get id
        """
        return self.__key

    @key.setter
    def id(self, key):
        '''
        set chain_id
        :param id:
        :return:
        '''
        self.__key = key

    @property
    def chain_id(self):
        """
        get id
        """
        return self.__chain_id

    @chain_id.setter
    def id(self, chain_id):
        '''
        set chain_id
        :param id:
        :return:
        '''
        self.__chain_id = chain_id

    @property
    def chain_storage(self):
        """
        get id
        """
        return self.__chain_storage

    @chain_storage.setter
    def chain_storage(self, chain_storage):
        '''
        set chain_id
        :param id:
        :return:
        '''
        self.__chain_storage = chain_storage

    @property
    def key_storage(self):
        """
        get id
        """
        return self.__keys_storage

    @key_storage.setter
    def id(self, keys_storage):
        '''
        set chain_id
        :param id:
        :return:
        '''
        self.__keys_storage = keys_storage

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def get_storage(self):

        return self.__chain_storage

    def is_valid(self, block_from_db):
        signature_db = block_from_db['signature']
        tmp_list = []
        tmp_list.append(block_from_db['data'].decode('utf-8'))
        tmp_list.append(str(block_from_db['timestamp']))
        tmp_list.append(str(block_from_db['prev_hash']))
        tmp_list.append(str(block_from_db['height']))
        tmp_list.append(str(block_from_db['version']))
        data = str(''.join(tmp_list))
        print()
        return self.key.public_key.verify(
           from_base58(signature_db),
           codecs.decode(get_data_hash(data), 'hex'))
        #   return server_vk.verify(
        #    from_base58(signature_db),
        #   codecs.decode(get_data_hash(data), 'hex'))

    def add_block(self, block):
        self.__height += 1
        self.__chain_storage.add_block(block)

    def get_block_by_height(self, height):
        return self.__chain_storage.get_block_by_height(height)

    def get_block_by_hash(self, hash):
        return self.__chain_storage.get_block_by_hash(hash)

    def create__block(self, version, data, prev_hash, timestamp, height):
        block = Block()
        block.set_version(version)
        block.set_data(data)
        block.set_prev_hash(prev_hash)
        block.set_timestamp(timestamp)
        block.set_height(height)
        block.set_signature(self.key.secret_key)
        block.set_hash_value()
        return block

    def create_genesis_block(self):
        genesis_block = Block()
        genesis_block.set_version(1)
        genesis_block.set_data(bytes('Talk is cheap', encoding='utf-8'))
        genesis_block.set_prev_hash('0')
        genesis_block.set_timestamp(1537016400)
        genesis_block.set_height(1)
        genesis_block.set_signature(self.key.secret_key)
        genesis_block.set_hash_value()
        return genesis_block


def print_block(block):
    print('version: ', block.get_version(), '\n')
    print('data: \n', block.get_data().decode("utf-8"), '\n')
    print('prev_hash: ', block.get_prev_hash(), '\n')
    print('timestamp: ', block.get_timestamp(), '\n')
    print('height: ', block.get_height(), '\n')
    print('signature: ', block.get_signature(), '\n')
    print('hash_value: ', block.get_hash_value(), '\n')


for j in range(1, 5):
    print('chain:', j)
    key = Key(j)
    blockchain_1 = Blockchain(key)
    blockchain_1.key_storage.add_key(blockchain_1.key)
    blockchain_1.key_storage.get_key(j)
    largest_heigth = blockchain_1.get_storage().get_largest_heigth()
    blockchain_1.set_height(largest_heigth)
    genesis_block = Block()
    if (largest_heigth == 0):
        genesis_block = blockchain_1.create_genesis_block()
        blockchain_1.add_block(genesis_block)
    else:
        genesis_block = blockchain_1.get_storage().get_block_by_height(1)

    #  print_block(genesis_block)
    pre_hash_value = genesis_block.get_hash_value()
    print('first db ', pre_hash_value)
    # key = Key()
    # key.set_key_pairs_by_generate(1)

    for i in range(10):
        data = str(blockchain_1.get_height() + 1) + \
               '  zhaoccai czhaoaw@connnect.ust.hk'
        #  tmp_data = ['username', 'zc', 'email', 'czhaoaw@connect.ust.hk', ]
        #  data = ''.join(tmp_data)
        #  data = json.dumps(tmp_data, sort_keys=True)
        block = blockchain_1.create__block(
            1,
            bytes(data, encoding='utf-8'),
            pre_hash_value,
            int(time.time()),
            blockchain_1.get_height() + 1)
        blockchain_1.add_block(block)
        pre_hash_value = block.get_hash_value()

    blockchain_1.get_storage().all_blocks()
    print('get by hash')
    block_from_db1 = blockchain_1.get_storage().get_block_by_height(1)
    block_from_db2 = blockchain_1.get_storage().get_block_by_height(2)
    block_from_db = blockchain_1.get_storage().get_block_by_hash(
        genesis_block.get_hash_value())
    print('after_db', genesis_block.get_hash_value())
    print(blockchain_1.is_valid(block_from_db))
    print(blockchain_1.is_valid(block_from_db2))
