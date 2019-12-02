import time
start_time = time.time()

import os
# Set up variables
file_one = "q:/blank2g.raw"
file_two = "q:/blank2g.raw"

chunk_size = 134217728  # number of bytes to read at once  64Mb

file_one_stat = os.stat(file_one)
file_one_size = file_one_stat.st_size
print("File one is: " + str(file_one_size) + " bytes")

file_two_stat = os.stat(file_two)
file_two_size = file_two_stat.st_size
print("File two is: " + str(file_two_size) + " bytes")

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
        if primary_buffer[loop] == secondary_buffer[loop]:
            hit += 1
    counter += chunk_size
print("Total matches: " + str(hit) + " which is approx: " + str(100*hit/counter) + "%")

f1.close()
f2.close()

print("time elapsed: {:.2f}s".format(time.time() - start_time))