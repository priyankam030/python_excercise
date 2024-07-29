'''Write a program to generate multipication table from 1 to 20 and 
 Write it to the diffrent files.
 place these files in a folder for a 13 - year old.
'''

def appendFile(file, string):
    f = open(file, "a")
    f.write(string)
    f.close()


for n in range (1,21):
    table_str  = ""
    for i in range(1, 11):
        table_str +=  str(n) + " X " + str(i) + " = " + (str)(n*i) + "\n" 

    fileName = "tables/table" + str(n) + ".txt"
    print(table_str)
    appendFile(fileName, table_str)

