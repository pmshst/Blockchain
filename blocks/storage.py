#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao

from interface import implements, Interface

class Storage(Interface):

    def save(self):
        pass

    def add_block(self):
        pass
    def all_blocks(self):
        pass
    def get_block_by_height(self):
        pass


class StorageDatabase(implements(Storage)):


    def save(self):
        pass

    def add_block(self):
        pass
    def all_blocks(self):
        pass
    def get_block_by_height(self):
        pass


class StorageFile(implements(Storage)):
    def save(self):
        pass

    def add_block(self):
        pass

    def all_blocks(self):
        pass

    def get_block_by_height(self):
        pass

