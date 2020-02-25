#!/local/cluster/bin/python3

# import required modules 
import sys
import io
import time

start = time.time()
# save all command line arguments in a list and assign respective variables to each input file 

#-------------------------------------------------------
#	Open each file recieved through CLI
#-------------------------------------------------------

arg_list = sys.argv
motif = io.open(arg_list[1])
bins = io.open(arg_list[2])
seq_file_list = arg_list[3:]

#-------------------------------------------------------
#	Read motif file and store motifs in a list
#-------------------------------------------------------

# Define list variable to store motif list
motif_list = []

# loop through file and append motif to the list
for ele in motif:
	motif_seq = ele.strip()
	motif_list.append(motif_seq)

#-------------------------------------------------------
#	Read Bin file and store bins in a list
#-------------------------------------------------------

bin_list = []
header = bins.readline()
for nums in bins:
	bin_range = nums.strip().split("\t")
	bin_list.append(bin_range)

#-------------------------------------------------------
#	Read sequence file and store seqs in list
#-------------------------------------------------------


seq_list = []

for files in seq_file_list:
	seq_file = io.open(files)
	for each_line in seq_file:
		line = each_line.strip()
		if not '>' in line:
			seq_list.append(line)

#-------------------------------------------------------
#	Loop through each motif_list for each kmer,
#	loop through each seq_list for each seq,
#	then set a sliding window for kmer matching
#	and if kmer match with sliding window, then 
#	count it and put it into repective bin.
#-------------------------------------------------------


for each_kmer in motif_list:

	# set count for each bin to 0 for each kmer
	count_0_5 = 0
	count_6_10 = 0
	count_11_15 = 0
	count_16_20 = 0
	count_21_25 = 0
	count_25_and_above = 0

	# set a sliding window for each kmer and count its occurances
	for each_seq in seq_list:
		count = 0
		for letter in range(0, len(each_seq), 1):
			kmer = each_seq[letter:letter+len(each_kmer)]
			if kmer == each_kmer:
				count += 1
		if (int(bin_list[0][0]) <= count <= int(bin_list[0][1])):
			count_0_5 += 1
	
		elif (int(bin_list[1][0]) <= count <= int(bin_list[1][1])):
			count_6_10 += 1
		
		elif (int(bin_list[2][0]) <= count <= int(bin_list[2][1])):
			count_11_15 += 1

		elif (int(bin_list[3][0]) <= count <= int(bin_list[3][1])):
			count_16_20 += 1
		
		elif (int(bin_list[4][0]) <= count <= int(bin_list[4][1])):
			count_21_25 += 1
		
		elif (int(bin_list[4][1]) < count):
			count_25_and_above += 1

	# open file for writing with kmer name and write respective 
	# informtion to file with proper tab and new line character
	out_fh = io.open(each_kmer, "w+")	
	out_fh.write("Low\tHigh\tNumber_of_Observations\n")
	out_fh.write(f"{bin_list[0][0]}\t{bin_list[0][1]}\t{count_0_5}\n")
	out_fh.write(f"{bin_list[1][0]}\t{bin_list[1][1]}\t{count_6_10}\n")
	out_fh.write(f"{bin_list[2][0]}\t{bin_list[2][1]}\t{count_11_15}\n")
	out_fh.write(f"{bin_list[3][0]}\t{bin_list[3][1]}\t{count_16_20}\n")
	out_fh.write(f"{bin_list[4][0]}\t{bin_list[4][1]}\t{count_21_25}\n")
	out_fh.write(f"{bin_list[4][1]}+\t\t{count_25_and_above}\n")
	out_fh.close()

# This gives us time required to run this program
end = time.time()
time2comp = round((end - start), 2)
num_of_files = len(seq_file_list)
print(f"Time required to run this program is {time2comp} seconds when {num_of_files} sequence file/s provided.")
