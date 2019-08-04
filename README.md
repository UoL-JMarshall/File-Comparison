# File-Comparison
Quick tool to help compare two files at bit level, as part of UoL MSc CyberSecurity dissertation project.

** Disclaimer:
This software is provided 'as is' and with no warranties of any kind, whether express or implied, including and without limitation, any warranty of merchantability or fitness for a particular purpose. The user (you) must assume the entire risk of using the software. In no event shall any individual, company or organization involved in any way in the development, sale or distribution of this software be liable for any damages whatsoever relating to the use, misuse, or inability to use this software (including, without limitation, damages for loss of profits, business interruption, loss of information, or any other loss). In short, I am not a professional programmer so use at your own risk!

This scipt can be used to examine two memory files, to compare the differences, and output a text file containing the differences, along with a graphical output. 

** Usage
To use this scipt change the following variables:

- Line 4 : The name and location of the first memory fragment.
- Line 5 : THe name and location of the second memory fragment.
- Line 6 : The name and location of the comparison results file.
- Line 7 : Chunk size.
- Line 8 : Image depth.

** Explanation of the script
- First the script will determin which of the 2 files is shorter, and denote that as the primary.
- Next, the script will determine how long to make the graphical outpt. Each pixel represents chunk_size worth of bits, compared, and coloured according to the number of differences. Each column will contain (chunk_size * image_depth) worth of memory bits. The initial output will be black, and based on the longer files length.
- Starting at position 0 (counter) the files are compared byte by byte
- If they are different a counter (bytes_differ) is increased.
- Once the desired number of bytes has been compared (chunk_size) the script outputs the results as a file summary, and colours the graphic pixel
- This cycle repeats until the shorter file has been processed.
- Any remaining bytes (of the longer file) are marked as differences.
