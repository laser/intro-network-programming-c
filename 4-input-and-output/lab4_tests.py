#!/usr/bin/env python

import unittest
import subprocess
import os
import tempfile

# create the database file
fd, name = tempfile.mkstemp()
os.close(fd)
database_file_path = name


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.add_binary_path = '{}/cmake-build-debug/db-add'.format(os.getcwd())
        self.lookup_binary_path = '{}/cmake-build-debug/db-lookup'.format(os.getcwd())

    def test_add_things(self):
        process = subprocess.Popen([self.add_binary_path, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='erin\nhello!\n')[0].split('\n')

        self.assertEqual(len(output), 2)
        self.assertEqual(output[0],
                         'name please (will truncate to 15 chars): msg please (will truncate to 23 chars):    1: {erin} said {hello!}')
        self.assertEqual(output[1], '')

        process = subprocess.Popen([self.add_binary_path, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='jamiroquai\nmellow\n')[0].split('\n')

        self.assertEqual(len(output), 2)
        self.assertEqual(output[0],
                         'name please (will truncate to 15 chars): msg please (will truncate to 23 chars):    2: {jamiroquai} said {mellow}')
        self.assertEqual(output[1], '')

    def test_lookup_hit_name_field(self):
        process = subprocess.Popen([self.lookup_binary_path, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='erin\n')[0].split('\n')

        self.assertEqual(len(output), 2)
        self.assertEqual(output[0], 'lookup:    1: {erin} said {hello!}')
        self.assertEqual(output[1], 'lookup: ')

    def test_lookup_hit_msg_field(self):
        process = subprocess.Popen([self.lookup_binary_path, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='hel\n')[0].split('\n')

        self.assertEqual(len(output), 2)
        self.assertEqual(output[0], 'lookup:    1: {erin} said {hello!}')
        self.assertEqual(output[1], 'lookup: ')

    def test_lookup_multiple_hits(self):
        process = subprocess.Popen([self.lookup_binary_path, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='ello\n')[0].split('\n')

        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], 'lookup:    1: {erin} said {hello!}')
        self.assertEqual(output[1], '   2: {jamiroquai} said {mellow}')
        self.assertEqual(output[2], 'lookup: ')

    def test_lookup_truncates_input(self):
        process = subprocess.Popen([self.lookup_binary_path, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='hellooooooooooooooo\n')[0].split('\n')

        self.assertEqual(len(output), 2)
        self.assertEqual(output[0], 'lookup:    1: {erin} said {hello!}')
        self.assertEqual(output[1], 'lookup: ')


if __name__ == '__main__':
    unittest.main()
