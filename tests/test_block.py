#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao
import unittest
from ..blocks.block import Block



class TestBlock(unittest.TestCase):

     def test_create_block(self):
         block=Block()

         block.set_version(0)
         self.assertEqual(0,block.get_version())

         block.set_payload(['D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY6',])
         self.assertEqual(['D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY6',], block.get_payload())


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


         '''self.payload = payload  # payload store data
         self.prev_hash = prev_hash
         self.timestamp = timestamp
         self.signature = signature
         self.hash_value = hash_value
         self.height = height'''
         '''
         return Block(0,['D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY6',],'GKud7tATKAtSkfVEeLA9PHcTMeJ9K51Uv',time.time(),\
                       'D7JRxt4Gr5hPKXequ7zYfyuv56xj3sqY6','F9JZR433daa7n3wM1oqabqTZh2tdG67r1',1)
         '''

if __name__ == "__main__":
        unittest.main()

