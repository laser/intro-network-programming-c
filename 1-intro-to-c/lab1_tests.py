#!/usr/bin/env python

import unittest
import subprocess
import os


class TestNumbers(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/numbers'.format(os.getcwd())

    def test_case_one(self):
        process = subprocess.Popen([self.binary_path, '12', '13'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'You typed in 12 and 13.\n')
        self.assertEqual(output[1], 'The average is 12.500000.\n')
        self.assertEqual(output[2], 'The first number, 12, is NOT prime.\n')
        self.assertEqual(output[3], 'The second number, 13, is prime.\n')
        self.assertEqual(output[4], '12 and 13 are relatively prime.\n')

    def test_case_two(self):
        process = subprocess.Popen([self.binary_path, '21', '22'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'You typed in 21 and 22.\n')
        self.assertEqual(output[1], 'The average is 21.500000.\n')
        self.assertEqual(output[2], 'The first number, 21, is NOT prime.\n')
        self.assertEqual(output[3], 'The second number, 22, is NOT prime.\n')
        self.assertEqual(output[4], '21 and 22 are relatively prime.\n')

    def test_case_three(self):
        process = subprocess.Popen([self.binary_path, '12', '14'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'You typed in 12 and 14.\n')
        self.assertEqual(output[1], 'The average is 13.000000.\n')
        self.assertEqual(output[2], 'The first number, 12, is NOT prime.\n')
        self.assertEqual(output[3], 'The second number, 14, is NOT prime.\n')
        self.assertEqual(output[4], '12 and 14 are NOT relatively prime.\n')


class TestConvert(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/convert'.format(os.getcwd())

    def test_case_one(self):
        process = subprocess.Popen([self.binary_path],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        output = process.communicate(input='-1')[0].split('\n')

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'signed dec:    -1')
        self.assertEqual(output[1], 'unsigned dec:  4294967295')
        self.assertEqual(output[2], 'hex:           ffffffff')
        self.assertEqual(output[3], 'binary:        1111 1111 1111 1111 1111 1111 1111 1111')
        self.assertEqual(output[4], '')

    def test_case_two(self):
        process = subprocess.Popen([self.binary_path],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE)

        output = process.communicate(input='1')[0].split('\n')

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'signed dec:    1')
        self.assertEqual(output[1], 'unsigned dec:  1')
        self.assertEqual(output[2], 'hex:           1')
        self.assertEqual(output[3], 'binary:        0000 0000 0000 0000 0000 0000 0000 0001')
        self.assertEqual(output[4], '')

    def test_case_three(self):
        process = subprocess.Popen([self.binary_path],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        output = process.communicate(input='100')[0].split('\n')

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], 'signed dec:    100')
        self.assertEqual(output[1], 'unsigned dec:  100')
        self.assertEqual(output[2], 'hex:           64')
        self.assertEqual(output[3], 'binary:        0000 0000 0000 0000 0000 0000 0110 0100')
        self.assertEqual(output[4], '')


if __name__ == '__main__':
    unittest.main()
