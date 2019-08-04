from PIL import Image

# User variables
File_One = "./file_one.txt"
File_Two = "./file_two.txt"
File_Comparison_Results = "./File_Comparison_Results.txt"
chunk_size = 1
image_depth = 1

# Script variables
counter = 0
bytes_differ = 0
chunk = 0
chunk_counter = 0
current_row = 0
current_column = 0
row_value = chunk_size * image_depth

# Read both files into memory
in_master = open(File_One, 'rb')
data_one = in_master.read()
print("Len Master:" + str(len(data_one)))
in_master = open(File_Two, 'rb')
data_two = in_master.read()
print("Len SNapshot:" + str(len(data_two)))
out_results = open(File_Comparison_Results, "w")

if len(data_one) <= len(data_two):
    primary = data_one
    secondry = data_two
    print("Primary is master")
else:
    primary = data_two
    secondry = data_one
    print("Primary is snapshot")

# Check to see if the longer file is divisible exactly by the row_value
if len(secondry) % row_value == 0:
    image_width = int((len(primary) - (len(primary) % row_value))/row_value)
else:
    image_width = int((len(primary) - (len(primary) % row_value))/row_value) + 1

# Status information
print("L:" + str(len(primary)) + " W:" + str(image_width) + " D:" + str(image_depth) +
      " Chunks:" + str(int(len(primary) / chunk_size)))

# Initialise the graphical display for the output
img = Image.new('RGB', [image_depth, image_width], "black")  # create a new black image
pixels = img.load()


while counter < len(primary):
    # Compare the bytes at location (counter) in both files
    if primary[counter] != secondry[counter]:
        bytes_differ += 1
    chunk_counter += 1

    # Check to see if the pixel grouping (chunk_size) has been reached and process
    if chunk_counter >= chunk_size:
        # Reset the counters and write the results to the file
        chunk += 1
        chunk_counter = 0
        out_results.write("Chunk " + str(chunk) + " : Differences: " + str(bytes_differ) + "\n")

        # Determine what colour to use based on the number of differences
        if bytes_differ == 0:  # no differences
            colourR, colourG, colourB = 255, 255, 255
        elif bytes_differ / chunk_size > .75:  # mostly different - black
            colourR, colourG, colourB = 0, 0, 0
        elif bytes_differ / chunk_size > .50:  # 50/50 - red
            colourR, colourG, colourB = 255, 0, 0
        elif bytes_differ / chunk_size > .25:  # most same - green
            colourR, colourG, colourB = 0, 255, 0
        else:  # high percentage the same
            colourR, colourG, colourB = 0, 0, 255

        # Colour the appropriate pixel
        pixels[current_row, current_column] = (colourR, colourG, colourB)
        current_row += 1

        # Once the image depth has been reached, move along 1 column and reset back to row 0
        if current_row >= image_depth:
            current_row = 0
            current_column += 1
        # Reset the differences counter
        bytes_differ = 0

    counter += 1
print("Exit chunk number: " + str(chunk))

# If a block of memory is being processed (ie chunk is not full) output what you have
if chunk_counter != 0:
    out_results.write("Chunk " + str(chunk_counter) + " : Differences: " + str(bytes_differ) + "\n")

# If the primary file was shorter, the remaining bytes are classified as differences
if counter < len(secondry):
    out_results.write("Remaining bytes: " + str(len(secondry) - counter) + "\n")

out_results.close()
img.show()
