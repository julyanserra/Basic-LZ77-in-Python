#Julian Serra: jserra17@cmc.edu
#LZ77

import struct
import sys
import math

def LZ77_search(search, look_ahead):

	 ls = len(search)
	 llh = len(look_ahead)
 
	 if(ls==0):
	 	return (0,0, look_ahead[0])
	 
	 if(llh)==0:
	 	return (-1,-1,"")

	 best_length=0
	 best_offset=0 
	 buf = search + look_ahead

	 search_pointer = ls	
	 #print( "search: " , search, " lookahead: ", look_ahead)
	 for i in range(0,ls):
	 	length = 0
	 	while buf[i+length] == buf[search_pointer +length]:
	 		length = length + 1
	 		if search_pointer+length == len(buf):
	 			length = length - 1
	 			break
	 		if i+length >= search_pointer:
	 			break	 
	 	if length > best_length:
	 		best_offset = i
	 		best_length = length

	 return (best_offset, best_length, buf[search_pointer+best_length])



def main():
	#extra credit
	x = 16
	MAXSEARCH = int(sys.argv[2])
	MAXLH =  int(math.pow(2, (x  - (math.log(MAXSEARCH, 2))))) 

	file_to_read = sys.argv[1] 
	input = parse(file_to_read)
	file = open("compressed.bin", "wb")
	searchiterator = 0;
	lhiterator = 0;

	while lhiterator<len(input):
		search = input[searchiterator:lhiterator]
		look_ahead = input[lhiterator:lhiterator+MAXLH]
		(offset, length, char) = LZ77_search(search, look_ahead)
		#print (offset, length, char)
		
		shifted_offset = offset << 6
		offset_and_length = shifted_offset+length 
		ol_bytes = struct.pack(">Hc",offset_and_length,char)  
		file.write(ol_bytes) 
		 

		lhiterator = lhiterator + length+1
		searchiterator = lhiterator - MAXSEARCH

		if searchiterator<0:
			searchiterator=0
		 	

	file.close()
		 

def parse(file):
	r=[]
	f = open(file, "rb" )
	text = f.read()
	return text

if __name__== "__main__":
	main()
 
