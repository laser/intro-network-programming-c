#!/usr/bin/env python

import unittest
import subprocess
import os


class TestIsort(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/isort'.format(os.getcwd())

    def test_outputs_three_lists(self):
        process = subprocess.Popen([self.binary_path],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.communicate(input='5')[0].split('\n')

        self.assertEqual(len(output), 4)
        self.assertRegexpMatches(output[0], "original: (\d+), (\d+), (\d+), (\d+), (\d+)")
        self.assertRegexpMatches(output[1], "ascending: (\d+), (\d+), (\d+), (\d+), (\d+)")
        self.assertRegexpMatches(output[2], "descending: (\d+), (\d+), (\d+), (\d+), (\d+)")
        self.assertEqual(output[3], "")


class TestTwecho(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/twecho'.format(os.getcwd())

    def test_upcases_each_argument(self):
        process = subprocess.Popen([self.binary_path, "hey", "dude", "bingo"],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output = process.stdout.readlines()

        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], 'hey HEY\n')
        self.assertEqual(output[1], 'dude DUDE\n')
        self.assertEqual(output[2], 'bingo BINGO\n')

    def test_missing_argument(self):
        process = subprocess.Popen([self.binary_path],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        process.communicate()

        self.assertEqual(process.returncode, 1)


if __name__ == '__main__':
    unittest.main()
