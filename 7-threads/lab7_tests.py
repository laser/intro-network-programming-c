#!/usr/bin/env python

import unittest
import subprocess
import os
import tempfile
import socket
import time
import httplib


def is_port_bound(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
        s.close()
        return False
    except socket.error as ex:
        return True


def wait_until(condition, timeout=5.0):
    end_time = time.time() + timeout
    status = condition()
    while not status and time.time() < end_time:
        time.sleep(0.3)
        status = condition()
    return status


def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


class TestThreadedServer(unittest.TestCase):

    def setUp(self):
        self.binary_path = '{}/cmake-build-debug/db-server'.format(os.getcwd())

    def test_server(self):
        # get an unbound port
        port = get_open_port()

        # create the database file
        fd, name = tempfile.mkstemp()
        os.close(fd)
        database_file_path = name

        process = subprocess.Popen([self.binary_path, "{}".format(port), "{}".format(database_file_path)],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        try:
            wait_until(lambda: is_port_bound("127.0.0.1", port))

            # create the first record
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("POST", "/records", "abou,howdy", {"Content-Type": "text/csv"})
            response = conn.getresponse()
            self.assertEqual(response.status, 201)

            # create the second record
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("POST", "/records", "joe,howaboutit?", {"Content-Type": "text/csv"})
            response = conn.getresponse()
            self.assertEqual(response.status, 201)

            # create the third record
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("POST", "/records", "kara,birds!", {"Content-Type": "text/csv"})
            response = conn.getresponse()
            self.assertEqual(response.status, 201)

            # get the third record by its database id (1, 2, 3, etc.)
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("GET", "/records/3")
            response = conn.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), "3,kara,birds!\r\n")
            self.assertEqual(response.getheader("Content-Length"), "15")

            # no record with the provided id exists
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("GET", "/records/42")
            response = conn.getresponse()
            self.assertEqual(response.status, 404)

            # query for records by substring (match two messages)
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("GET", "/records?q=how")
            response = conn.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), "1,abou,howdy\r\n2,joe,howaboutit?\r\n")
            self.assertEqual(response.getheader("Content-Length"), "33")

            # query for records by substring (match with one name and one message)
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("GET", "/records?q=abou")
            response = conn.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), "1,abou,howdy\r\n2,joe,howaboutit?\r\n")
            self.assertEqual(response.getheader("Content-Length"), "33")

            # query produced no matches
            conn = httplib.HTTPConnection("127.0.0.1:{}".format(port))
            conn.request("GET", "/records?q=notgonnamatch")
            response = conn.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), "")
            self.assertEqual(response.getheader("Content-Length"), None)

        finally:
            process.kill()


if __name__ == '__main__':
    unittest.main()
