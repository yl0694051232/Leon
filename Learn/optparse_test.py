import optparse

usage = "myprog[ -f <filename>][-s <xyz>] arg1[,arg2..]"
parser = optparse.OptionParser(usage,version="1.0")
parser.add_option("-f", "--file",action="store", type="string", dest="filename",default="foo.txt",help = "readline all the files.",metavar="FILE")
parser.add_option("-q", "--quiet",action="store_false", dest="verbose", default=True,help="don't print status messages to stdout")
parser.add_option("-i","--increment",dest = "value",action = "count")

(options, args) = parser.parse_args()

print ("value",options.value)
print (options.filename)
print (options.verbose)











