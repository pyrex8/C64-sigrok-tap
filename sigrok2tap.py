
# Bytes: 
# $0000-$000B: File signature "C64-TAPE-RAW"
#        $000C: TAP version (see below for description)
#               $00 - Original layout
#               $01 - Updated
# $000D-$000F: Future expansion
# $0010-$0013: File  data  size  (not  including  this  header,  in
#              LOW/HIGH format) i.e. This image is $00082151  bytes
#                        long.
# $0014-$xxxx: File data






with open("print_h.tap", "rb") as f:
    fileSignature = f.read(12)
    print fileSignature
    tapVersion = f.read(1)
    print 'TAP Version',ord(tapVersion)
    futureExpansion = f.read(2)
    fileSize = f.read(4)
    #    totalSize = ord(fileSize[3])+ord(fileSize[2])+ord(fileSize[1]),hex(ord(fileSize[0]))
    print "size: $%02x%02x%02x%02x" % (ord(fileSize[3]),
    	ord(fileSize[2]), ord(fileSize[1]), ord(fileSize[0]))
