 
Julian Serra

This is a very basic LZ77 encoder and decoder that achieves a solid compression ratio for small files.

Running the program:

In the command line:

	python encoder.py 'x' 'y'
	
	x = name of file
	y = size of max search buffer, i.e. 1024

This will output the compressed file under the name 'compressed.bin'

to decode this compressed file, in the command line:

	python decoder2.py "x" "y" 
	
	x = size of max search buffer used in encoder, i.e. 1024
	y = file type, i.e. txt, jpg, etc.

This will output a file called 'processed.txt' or 'processed.jpg', etc. 
	
	
This should be your decompressed file which is exactly the same as the original file you compressed.
 
 
