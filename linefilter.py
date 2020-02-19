########################################
#    rootedshell | rajeshd.in          #
########################################

# Filter lines from text file

# Replace the "word1, word2","wordn" to filter the line
strings = ("word1", "word2", "dwordn")

newLines = []

# Replace the file name
with open('sample.txt') as f:
    try:
        for line in f:
            if any(s in line for s in strings):
                newLines.append(line)
    except:
        pass
        
f.close()

theFile = open('linefilter_op.txt' , 'w')
for line in newLines:
    theFile.write(line)
    
theFile.close()

print("Done!")

