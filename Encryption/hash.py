#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This script demonstrates how to generate a hash using different algorithms
# and how to create a salt for hashing purposes.
import hashlib
import os
def generate_a_salt():
    salt = os.urandom(16)
    str_salt = str(salt)
    encoded_string = str_salt.encode()
    return bytearray(encoded_string)  # The salt is returned as a byte_array
message_to_hash=b'Jonathan'

md5_hasher = hashlib.md5(message_to_hash)
print("MD5 hash: ", md5_hasher.hexdigest())

sha1_hasher= hashlib.sha1(message_to_hash)
print("SHA1 hash: ", sha1_hasher.hexdigest())

sha256_hasher= hashlib.sha256(message_to_hash)
print("SHA256 hash: ",sha256_hasher.hexdigest())
