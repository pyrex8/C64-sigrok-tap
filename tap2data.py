# -*- coding: utf-8 -*-
"""TAP file to data print utility. This is just to see the data in a .TAP file

Bytes:
$0000-$000B: File signature "C64-TAPE-RAW"
        $000C: TAP version (see below for description)
               $00 - Original layout
               $01 - Updated
 $000D-$000F: Future expansion
 $0010-$0013: File  data  size  (not  including  this  header,  in
              LOW/HIGH format) i.e. This image is $00082151  bytes
                        long.
 $0014-$xxxx: File data"""

import re

def main():
    """ Main"""
    with open("print_h.tap", "rb") as tap_file:
        tap_file.seek(0, 2)
        tap_file_length = tap_file.tell()
        print "total file length:", tap_file_length
        tap_file.seek(0)

        file_signature = tap_file.read(12)
        print file_signature
        tap_version = tap_file.read(3)
        print 'TAP Version', ord(tap_version[0])
#        future_expansion = tap_file.read(2)
        file_size = tap_file.read(4)
        file_size_bytes = (ord(file_size[3])<<24) + (ord(file_size[2])<<16) + \
        (ord(file_size[1])<<8) + ord(file_size[0])

        print "size: $%08x" % file_size_bytes,
        print "(" + str(file_size_bytes) +")"

        f1 = re.search(b'\x05', tap_file.read())

    print "found a match:", ord(f1.group())
    print "match offset:", f1.start()

if __name__ == '__main__':
    main()
