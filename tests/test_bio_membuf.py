#!/usr/bin/env python2.0

"""Unit tests for M2Crypto.BIO.MemoryBuffer.

Copyright (c) 2000 Ng Pheng Siong. All rights reserved."""

RCS_id='$Id: test_bio_membuf.py,v 1.1 2000/11/08 14:41:57 ngps Exp $'

import unittest
import M2Crypto
from M2Crypto.BIO import MemoryBuffer

class MemoryBufferTestCase(unittest.TestCase):

    def setUp(self):
        self.data = 'abcdef' * 64

    def tearDown(self):
        pass

    def check_init_empty(self):
        mb = MemoryBuffer()
        assert len(mb) == 0
        out = mb.read()
        assert out is None

    def check_init_something(self):
        mb = MemoryBuffer(self.data)
        assert len(mb) == len(self.data)
        out = mb.read()
        assert out == self.data

    def check_read_less_than(self):
        chunk = len(self.data) - 7
        mb = MemoryBuffer(self.data)
        out = mb.read(chunk)
        assert out == self.data[:chunk] and len(mb) == (len(self.data) - chunk)
        
    def check_read_more_than(self):
        chunk = len(self.data) + 8
        mb = MemoryBuffer(self.data)
        out = mb.read(chunk)
        assert out == self.data and len(mb) == 0

    def check_write_close(self):
        mb = MemoryBuffer(self.data)
        assert mb.writeable()
        mb.write_close()
        assert mb.readable()
        self.assertRaises(IOError, mb.write, self.data)
        assert not mb.writeable()

    def check_closed(self):
        mb = MemoryBuffer(self.data)
        mb.close()
        self.assertRaises(IOError, mb.write, self.data)
        assert not mb.readable() and not mb.writeable()


def suite():
    return unittest.makeSuite(MemoryBufferTestCase, 'check_')
    

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

