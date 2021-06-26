#!/usr/bin/env python3
 
import sys
import argparse

# Usage xor.py [-b|-t] file1 [-b|-t] file2 .... [-o outputfile|-to]
# xors the hex bytes in the (-b binary) or (-t ascii text formatted hex string without line breaks) input files and spits out a new file that is xored(-o outpufile), or the resulting xored hexstring (-to)
# example: xor.py -b binary1.bin -b binary2.bin -t text.txt -o outputfile.bin

ap = argparse.ArgumentParser()
ap.add_argument("-t","--text", action='append', nargs='+', required=False,help="text input file, hex string without line breaks")
ap.add_argument("-b","--binary", action='append', nargs='+', required=False,help="binary input file")
ap.add_argument("-o","--outputfile",required=False,help="output file")
ap.add_argument("-to","--textoutput", action='store_true',required=False,help="text output")

args = vars(ap.parse_args())
#options = [opts for opts in sys.argv[1:] if opts.startswith('-')]
#arguments = [args for args in sys.argv[1:] if not args.startswith('-')]

def importfile(file,options): #'r' or 'rb'
    with open(file,options) as file:
        if options == 'r':
            data = file.read().strip()
        elif options == 'rb':
            data = file.read().hex()
    return data

def texttohex(text):
    i=0
    texthex = []
    while i<len(text):
        texthex.append(text[i:i+2])
        i+=2
    return texthex

def xor(hexlista,hexlistb):
    xored = []
    shortestlen = 0
    if len(hexlista)<len(hexlistb):
        shortestlen = len(hexlista)
    elif len(hexlistb)<len(hexlista):
        shortestlen = len(hexlistb)
    elif len(hexlista) == len(hexlistb):
        shortestlen = len(hexlista)
    else:
        raise('length error between two lists error ')
    for i in range(shortestlen):
        xored.append(hex(int(hexlista[i],16)^int(hexlistb[i],16))[2:])
    return xored

def save(hexlist):
    intlist = [int(i,16) for i in hexlist]
    bytelist = bytes(intlist)
    with open(args["outputfile"],'wb') as writefile:
        writefile.write(bytelist)

def padhex(hexlist):
    processedlist = []
    for hex in hexlist:
        if len(hex)==2:
            processedlist.append(hex)
        if len(hex)<2:
            processedlist.append('0'+hex)
    return "".join(processedlist)
            
argdata = []
hexlist = []
xoredlist = []
def main():
    if args["binary"]:
        for i in range(len(args["binary"])):
            argdata.append(importfile(args["binary"][i][0],'rb'))
    
    if args["text"]:
        for i in range(len(args["text"])):
            argdata.append(importfile(args["text"][i][0],'r'))

    #print(argdata)
    
    for string in argdata:
        currlist = texttohex(string)
        hexlist.append(currlist)
    #print(hexlist)
    
    prevlist = hexlist[0]
    for i in range(len(hexlist)-1):
        currlist = xor(prevlist,hexlist[i+1])
        prevlist = currlist
        xoredlist.append(currlist)
    #print(xoredlist)
    
    if args["outputfile"]:
        save(xoredlist[-1])
    if args["textoutput"]:
        print(padhex(xoredlist[-1]))



if __name__ == "__main__":
    main()

