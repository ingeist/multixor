# multixor

 Usage xor.py [-b|-t] file1 [-b|-t] file2 .... [-o outputfile|-to]

 xors the hex bytes in the (-b binary) or (-t ascii text formatted hex string without line breaks) input files and spits out a new file that is xored(-o outpufile), or the resulting xored hexstring (-to)

 examples: 
 
 xor.py -b binary1.bin -b binary2.bin -t text.txt -o outputfile.bin
 
 xor.py -b binary.bin -t text1.txt text2.txt text3.txt -to
