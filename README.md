# File-Comparison
Tool written in Python 3 (with PIL library import) to help compare two files at bit level, as part of UoL MSc CyberSecurity dissertation project.

** Disclaimer:
This software is provided 'as is' and with no warranties of any kind, whether express or implied, including and without limitation, any warranty of merchantability or fitness for a particular purpose. The user (you) must assume the entire risk of using the software. In no event shall any individual, company or organization involved in any way in the development, sale or distribution of this software be liable for any damages whatsoever relating to the use, misuse, or inability to use this software (including, without limitation, damages for loss of profits, business interruption, loss of information, or any other loss). In short, I am not a professional programmer so use at your own risk!

----

Input:

-- Multiple memory fragments, all the same size, sequentially numbered the same

-- Change the 'filename' on line 64 to match the file names of the memory samples

-- Change the sequence range in line 59 (x, y)

-- Change the chunksize (line 27) depending on system ram to read in an amount of data at once (cache)

Output:

-- Console output listing the size of the files + the number of differences

 Execution:
 
-- Once started, the system will compare each file one by one.


-- For example:  if the range was (1, 5) then:

----- filename1 would be compared to filename2

----- filename2 would be compared to filename3

----- filename3 would be compared to filename4

----- Etc.
