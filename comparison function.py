# File Compare Function
# Written by: Jason Marshall
# Part of an MSC CyberSecurity
#
# Input:
#   Multiple memory fragments, all the same size, sequentially numbered the same (eg: Memory1.raw, Memory2.raw, Memory3.raw, etc.)
# Output:
#   Console output listing the size of the file + the number of differences
#
# Execution:
#   Change the 'filename' on line 64 to match the file name of the memory samples + change the sequence range in line 59 (x, y)
#   Once started, the system will compare each file one by one.
#   Change the chunksize (line 27) to read in a certain amount of data into memory at once.
#
#   For example:  if the range was (1, 5) then:
#      filename1 would be compared to filename2
#      filename2 would be compared to filename3
#      filename3 would be compared to filename4
#      Etc.

import time
import os


def comparefiles(file_one, file_two):
    start_time = time.time()
    chunk_size = 134217728  # number of bytes to read at once  64Mb
    file_one_stat = os.stat(file_one)
    file_one_size = file_one_stat.st_size
    print("File one (" + file_one + ") is: " + str(file_one_size) + " bytes")

    file_two_stat = os.stat(file_two)
    file_two_size = file_two_stat.st_size
    print("File two (" + file_two + ") is: " + str(file_two_size) + " bytes")

    if file_one_size != file_two_size:
        print("Error (2) Files not of the same size - aborting")
        exit(2)

    if file_one_size % chunk_size != 0:
        print("Error (3) Chunk size is not valid for selected files")
        exit(3)

    f1 = open(file_one, 'rb')
    f2 = open(file_two, 'rb')

    counter = 0
    hit = 0

    # Iterate through smaller file, comparing them byte by byte
    while counter < file_one_size:
        primary_buffer = f1.read(chunk_size)
        secondary_buffer = f2.read(chunk_size)
        for loop in range(0, chunk_size):
            if primary_buffer[loop] != secondary_buffer[loop]:
                hit += 1
        counter += chunk_size
    print("Total size: " + str(file_one_size) + " which had " + str(hit) + " differences")
    
    f1.close()
    f2.close()
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
    return(hit)


def main(filename):
    for filenum in range (x, y):
        comparefiles(filename+str(filenum)+".raw", filename+str(filenum+1)+".raw")
    return()


main('filemname')
