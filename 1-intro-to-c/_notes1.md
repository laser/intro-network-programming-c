# Week 1

## Key Concepts

- bytes and their encodings

## Reading

1. (required) K&R Chapters 1-4
2. (required) http://www.csc.villanova.edu/~mdamian/C/c-input-output.htm

## Lecture: Bytes and Encodings

### What's a Byte?

A byte is a unit of digital information that your CPU knows how to 
work with (add, multiple, substract, et cetera). Your CPU can do all 
sorts of things, but it doesn't do those things with numbers or 
strings or characters or cat pictures; your CPU works in bytes, and 
your programs need to take higher-level constructs like numbers and 
strings and cat pictures and convert them to bytes in order for that 
CPU to do anything useful.

Historically, the byte was the number of bits required to represent 
a single character of text in a computer and for this reason it is 
the smallest addressable unit of memory in many computer 
architectures. Today, a byte is almost always 8 bits of information.

Fun fact: Back in the day, a byte might be composed of some number 
of bits < 7. You may notice that certain networking-related RFCs use 
the term "octet" - this was to clarify that they were talking about 
an 8-bit chunk of data.

### Same Bytes, Many Representations

A sequence of bytes can be represented in a variety of different 
ways depending on the needs of the program. For example: Some bytes
might be represented as a base-64 string in order to send the bytes
over a channel that only supports text, like HTTP.

Assume for a moment that we have a sequence of three bytes whose 
base-2 ("binary") representation looks like this:

```c
01101111 01101001 00100001
```

This same sequence of bytes can be represented in many ways. For 
example, we could represent it as a sequence of base-10 ("decimal") 
numbers:

```c
111 105 33
```

...or we could represent the bytes as a base-16 ("hex") encoded
string:

```c
6f 69 21
```

...or we could represent the bytes as an ASCII-encoded string:

```c
oi!
```

The point that I'm trying to make is that the bits, in memory or on 
the disc, exist independently from how we encode and interpret them.

### Creating Sequences of Bytes

How does our terminal know what bytes to write to stdin when we type 
stuff, or how to render the bytes in a file when we `cat` its contents 
to stdout?

It all comes down to how you have your terminal configured! The 
terminal's character encoding determines how to turn keystrokes into 
bytes (for writing), and how to interpret bytes for display (when 
reading).

An example: Ensure that your terminal's character encoding is set to 
UTF-8, copy-paste this command into your shell, and then run it:

```shell
$ printf 'ᕗ' > /tmp/utf8.txt
```

This command writes the bytes corresponding to the UTF-8 encoded 
CANADIAN SYLLABICS FO character to the utf8.txt file. You can view a 
hex encoding of the file's contents by running xxd on that file:

```shell
$ xxd /tmp/utf8.txt
00000000: e195 97    
```

The file contains following bytes: `e1 95 97`.

Now, switch your terminal's character encoding to `Inuit (Mac OS)`
and copy-paste into the shell, changing the target file from utf8.txt 
to inuit.txt:

```shell
$ printf 'ᕗ' > /tmp/inuit.txt
```

Afterwards, run `xxd` on that new file:

```shell
$ xxd /tmp/inuit.txt
00000000: cf
```

Whoa! Two less bytes than in utf8.txt! What gives?

What's happened is that the ᕗ can be represented by a single byte if 
we're interpreting that glyph as a character in the Mac OS Inuit 
encoding (which is optimized for Inuit characters such as this), but 
if we're encoding the glyph as a UTF-8 character, it's going to take 
up 3 bytes.

A fun fact: The first 127 values of most character sets are encoded 
identically, and all letters of the English alphabet fit into that 
range. For example ASCII, UTF-8, and Mac OS Inuit all encode the 
letter 'a' using a single byte, 0x61.

### Things That Go Beep in the Night

A challenge to you: Do a little digging and figure out why you're
likely to hear a beep sound out of your terminal if you `cat` some
random binary. 

## Relating This to C

An unsigned integer in C takes up 4 bytes of space and can represent 
numbers in the range 0 to 4,294,967,295.

A binary encoding of the unsigned integer 1 would look like this:

```c
00000000 00000000 00000000 00000001
```

...and the binary encoding of the unsigned integer 4,294,967,295:

```c
11111111 11111111 11111111 11111111
```

A signed integer on the other hand shifts the whole range over and 
can be used to represent numbers between -2,147,483,648 and 
2,147,483,647 using the same number of bytes. A binary 
representation of the signed integer 1 would look the same as the 
unsigned integer 1:

```c
00000000 00000000 00000000 00000001
```

To convert between the bits for a positive number (1) to a negative 
number (-1), we take the two's complement of our bits (flip all the 
bits and then add 1), leaving us with:

```c
11111111 11111111 11111111 11111111
```

So who cares? What does this mean?

You'll notice that when we interpret the bits:

```c
11111111 11111111 11111111 11111111
```

...as an unsigned integer, we get 4,294,967,295 - but when we 
interpret them as a signed integer, we get -1.

This _interpretation_ happens in our programs all the time (C,
anyways). In the following example, we're telling the printf 
function to treat the bytes stored in `qq` as a signed integer, 
predictably producing the output "signed dec: -1." We then tell the 
computer to interpret those bytes as an unsigned integer, which 
yields the output "unsigned dec: 4294967295." The bytes themselves 
(stored in `qq`) haven't changed, but our interpretation of those bytes 
has.

```c
int qq = -1;
printf("signed dec:    %d\n", qq);
printf("unsigned dec:  %u\n", qq);
```
