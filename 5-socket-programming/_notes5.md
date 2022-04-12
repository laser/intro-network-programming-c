# Week 5

## Key Concepts

- TCP socket API (`connect`, `accept`, `read`, `write`)
- HTTP protocol

## Reading

1. (required) UNP Chapters 3-5
2. (optional) https://beej.us/guide/bgnet/html/#what-is-a-socket
3. (optional) https://beej.us/guide/bgnet/html/#ip-addresses-structs-and-data-munging
4. (optional) https://beej.us/guide/bgnet/html/#system-calls-or-bust

## Lecture

### TCP/IP Model of Networking

[RFC-1122: Requirements for Internet Hosts -- Communication Layers 
(1989)][1] describes a mechanism that computers can use to talk to 
each other over a network. It divides the network stack into 4 
layers:

Link (ARP)
Network (IP)
Transport (TCP, UDP)
Application (HTTP, FTP, DHCP)

We're going to focus on layers 3 and 4 today, specifically HTTP over TCP.

### [RFC-793: Transmission Control Protocol (1981)][2]

A TCP connection between two hosts allows for reliable transmission 
of ordered byte sequences across a network. The bytes are shuffled 
over the network using IP, but the error-checking and buffering 
required for ordering are provided by the TCP portion of your 
computer's networking stack. TCP is a stateful protocol and this 
state is managed by the OS kernel.

### HTTP

HTTP is a stateless, application-level protocol that piggybacks on 
the reliability of TCP to provide request/response-style 
communications between hosts.

### The TCP Socket API

We're going to get some exposure to socket programming by creating a 
basic TCP server using the lowest-level Ruby API we can find. Our 
TCP server will accept a connection from a client, read some test 
from that client, and echo that text back to the client.

Our server will need to:

- Create a TCP socket and corresponding file descriptor
- Bind that socket to a port
- Indicate that it is ready to accept incoming connections
- Accept a connection, creating a file descriptor for the client
- Read data from the client file descriptor
- Write data to the client file descriptor
- Close the client file descriptor, closing the TCP connection

```ruby
# server.rb
require "socket"

socket = Socket.new(Socket::AF_INET, Socket::SOCK_STREAM)
socket.setsockopt(:SOCKET, :REUSEADDR, true)
socket.bind(Socket.sockaddr_in(4444, "127.0.0.1"))
socket.listen(128)

loop do
 client_socket, _ = socket.accept
 client_socket.sendmsg "Please enter a string: "
 from_client = client_socket.gets
 client_socket.sendmsg "You said: #{from_client}\n"
 client_socket.close
end
```

We can use netcat to test our new TCP server:

```shell
$ ruby server.rb &

$ nc localhost 4444
Please enter a string: howdy
You said: howdy
```

### HTTP

For a computer to make an HTTP "request" to some other computer, it 
simply needs to establish a TCP connection to that other computer 
and to write an [RFC-2616][3]-compliant string to that connection.

```
Request-Line   = Method SP Request-URI SP HTTP-Version CRLF
               = GET /foo.html HTTP/1.1
               = GET http://www.example.com/foo.html HTTP/1.1
```

The server can "respond" by sending a CRLF-terminated string (also 
specified in RFC-2616) back to its client:

```
Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF
		= HTTP/1.1 200 OK
            = HTTP/1.1 404 NOT FOUND
```

For example, we can upgrade our TCP server to a basic HTTP server 
like so:

```ruby
require "socket"

server_socket = Socket.new(Socket::AF_INET, Socket::SOCK_STREAM)
server_socket.setsockopt(:SOCKET, :REUSEADDR, true)
server_socket.bind(Socket.sockaddr_in(4444, "127.0.0.1"))
server_socket.listen(128)

loop do
 client_socket, _ = server_socket.accept

 request_uri = client_socket.readline.split(" ")[1]

 response_body = "You made an HTTP request to #{request_uri}\r\n"

 response_string = <<~EOS.chomp
   HTTP/1.1 200 OK
   Content-Length: #{response_body.length}
   Connection: close
   Content-Type: text/plain

   #{response_body}
 EOS

 client_socket.write response_string
 client_socket.close
end
```

We can test it using the curl command:

```shell
$ ruby server.rb &

$ curl http://localhost:4444/foo/bar/baz
You made an HTTP request to /foo/bar/baz
```

[1]: https://datatracker.ietf.org/doc/html/rfc1122
[2]: https://datatracker.ietf.org/doc/html/rfc793
[3]: https://www.w3.org/Protocols/rfc2616/rfc2616

