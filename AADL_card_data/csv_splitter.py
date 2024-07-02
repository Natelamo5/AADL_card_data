csvfile = open('path', 'r').readlines()
# I explain how this works a little in the report, but this file is used to break up one big CSV into multiple CSV's. The 4877 in this case is the number of rows I was making each file
filename = 1
for i in range(len(csvfile)):
    if i % 4877 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+4877])
        filename += 1