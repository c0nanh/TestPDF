'''
Created on Dec 1, 2014

Searches for keywords in patterns for all the text files in a given directory.
Outputs to CSV file specified in fh for each keyword matched to each text file.
Ignores case

@author: pyonkichi
'''
import sys, os, glob, re, mmap

patterns = [ 'Myanmar', 'Burma', 'CSR', 'Social Responsibility', 'ESG', 'sustainable', 'sustainability' ]
working_dir = '/Users/pyonkichi/Dropbox/Ben/Reports'
fh = open("/Users/pyonkichi/Dropbox/Ben/ParseResults2.txt", "w")
os.chdir(working_dir)

heading = "Ticker, " + ", ".join(str(i) for i in patterns)
fh.write(heading + "\n")

for file in glob.glob('*.txt'):

    full_file_name = os.path.join(working_dir, str(file))

    with open(full_file_name, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)

        flag = [False] * len(patterns)

        for i in range(len(patterns)):
            
            #r'\bMyanmar\b' works
            #'\bMyanmar\b' does not work
            # '\\bMyanmar\\b' works
            if re.search('\\b' +patterns[i] + '\\b', data, flags=re.IGNORECASE):
                flag[i] = True

        ticker = str(file)[:-4]
        print "processing.... " + ticker
        fh.write(ticker + ", " + ", ".join(str(f) for f in flag) + "\n")
        fh.flush()        
        data.close()
        
fh.close()