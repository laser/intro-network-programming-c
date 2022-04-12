#!/usr/bin/env python

import unittest
import subprocess
import os

class TestRevecho(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/revecho'.format(os.getcwd())

    def test_contains_dude(self):
        process = subprocess.Popen([self.binary_path, "hello", "world", "dude"],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'dude\n')
        self.assertEqual(output[1], 'world\n')
        self.assertEqual(output[2], 'hello\n')
        self.assertEqual(output[3], '\n')
        self.assertEqual(output[4], 'dude found\n')

    def test_no_dude(self):
        process = subprocess.Popen([self.binary_path, "hello", "world", "gnar"],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'gnar\n')
        self.assertEqual(output[1], 'world\n')
        self.assertEqual(output[2], 'hello\n')
        self.assertEqual(output[3], '\n')
        self.assertEqual(output[4], 'dude not found\n')

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/linked-list-test'.format(os.getcwd())

    def test_outputs_expected_stuff(self):
        process = subprocess.Popen([self.binary_path],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 23)
        self.assertEqual(output[0], 'testing add_front(): 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 \n')
        self.assertEqual(output[1], 'testing flip_sign_double(): -9.0 -8.0 -7.0 -6.0 -5.0 -4.0 -3.0 -2.0 -1.0 \n')
        self.assertEqual(output[2], 'testing flip_sign_double() again: 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 \n')
        self.assertEqual(output[3], 'testing find_node(): OK\n')
        self.assertEqual(output[4], 'popped 9.0, the rest is: [ 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 ]\n')
        self.assertEqual(output[5], 'popped 8.0, the rest is: [ 7.0 6.0 5.0 4.0 3.0 2.0 1.0 ]\n')
        self.assertEqual(output[6], 'popped 7.0, the rest is: [ 6.0 5.0 4.0 3.0 2.0 1.0 ]\n')
        self.assertEqual(output[7], 'popped 6.0, the rest is: [ 5.0 4.0 3.0 2.0 1.0 ]\n')
        self.assertEqual(output[8], 'popped 5.0, the rest is: [ 4.0 3.0 2.0 1.0 ]\n')
        self.assertEqual(output[9], 'popped 4.0, the rest is: [ 3.0 2.0 1.0 ]\n')
        self.assertEqual(output[10], 'popped 3.0, the rest is: [ 2.0 1.0 ]\n')
        self.assertEqual(output[11], 'popped 2.0, the rest is: [ 1.0 ]\n')
        self.assertEqual(output[12], 'popped 1.0, the rest is: [ ]\n')
        self.assertEqual(output[13], 'testing add_after(): 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 \n')
        self.assertEqual(output[14], 'popped 1.0, and reversed the rest: [ 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 ]\n')
        self.assertEqual(output[15], 'popped 9.0, and reversed the rest: [ 2.0 3.0 4.0 5.0 6.0 7.0 8.0 ]\n')
        self.assertEqual(output[16], 'popped 2.0, and reversed the rest: [ 8.0 7.0 6.0 5.0 4.0 3.0 ]\n')
        self.assertEqual(output[17], 'popped 8.0, and reversed the rest: [ 3.0 4.0 5.0 6.0 7.0 ]\n')
        self.assertEqual(output[18], 'popped 3.0, and reversed the rest: [ 7.0 6.0 5.0 4.0 ]\n')
        self.assertEqual(output[19], 'popped 7.0, and reversed the rest: [ 4.0 5.0 6.0 ]\n')
        self.assertEqual(output[20], 'popped 4.0, and reversed the rest: [ 6.0 5.0 ]\n')
        self.assertEqual(output[21], 'popped 6.0, and reversed the rest: [ 5.0 ]\n')
        self.assertEqual(output[22], 'popped 5.0, and reversed the rest: [ ]\n')

if __name__ == '__main__':
    unittest.main()
