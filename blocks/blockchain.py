#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leo Zhao


import time
import hashlib
import json
from .key import Key
from .storage import *


class Blockchain:

    key = Key()
    storage = StorageDatabase()
    height=0
    def __init__(self):
        return self
    def is_valid(self):
        pass