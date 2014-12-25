import os, glob

working_dir = '/Users/pyonkichi/Dropbox/Ben/Reports'
os.chdir(working_dir)

for file in glob.glob('*.pdf'):
    text_name = file.rsplit( ".", 1 )[ 0 ] + ".txt"
    print("Processing..." + str(file))
    os.system("pdf2txt.py -n -o " + text_name + " " + str(file))
    