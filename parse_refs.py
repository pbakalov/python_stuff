file = open("slavery_in_the_ottoman_empire.txt", 'r')

begin_ref = "<ref>"
end_ref = "</ref>"
begin_ref2 = "<ref"
end_ref2 = "/>"

begin_indices = []
refs = []
refs_repeated = []
line_count = 0
for line in file:
    for index, char in enumerate(line):
        #if char == "<":
        if line[index:index+5] == begin_ref:
            #print line[index:index+20]
            for index2, char2 in enumerate(line[index+5:]):
                if char2 == "<":
                    #print "char2", line[index+5+index2:index+5+index2+10]
                    if line[index+5+index2:index+5+index2+6] == end_ref:  
                        #print "two", line[index+5+index2:index+5+index2+10]
                        refs.append(line[index:index+index2+11])
                        break
        elif line[index:index+4] == begin_ref2:
            for index2, char2 in enumerate(line[index+4:]):
                if line[index+4+index2:index+4+index2+2] == end_ref2:  
                    refs_repeated.append(line[index:index+index2+6])
                    break
                elif line[index+4+index2:index+4+index2+6] == end_ref:  
                    refs.append(line[index:index+index2+10])
                    break
    line_count+=1

file.close()
for ind, ref in enumerate(refs):
    print ind+1,ref, "\n"

for ind, ref in enumerate(refs_repeated):
    print ind+1, ref, "\n"
