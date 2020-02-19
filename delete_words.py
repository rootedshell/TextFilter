########################################
#    rootedshell | rajeshd.in          #
########################################

# Filter lines from text file

# Change the input file name
infile = "linefilter_op.txt"

outfile = "cleaned_file.txt"


# Enter sample words to delete from the file
delete_list = ["word1:", "word2:", "dwordn:"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
        
    fout.write(line)
fin.close()
fout.close()

print("Done!")