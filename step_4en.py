import os, glob, re
from bs4 import BeautifulSoup

path = 'english3/'
dest_path = 'english/'
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
      cleaner_filename = filename.replace("english3/", "")
      filename_destination = dest_path + cleaner_filename
      file2 = open(filename_destination,'w')
      data = f.readlines()
      for n, line in enumerate(data):
         if line.startswith(' '):
            data[n] = line.lstrip()
      for n, line in enumerate(data):
         data[n] = ''.join(line.split('  '))
      x = ''.join(data)
      x =  "".join(line for line in data if not line.isspace())
      file2.seek(0)
      file2.write(x)  
   pre, ext = os.path.splitext(filename_destination)
   os.rename(filename_destination, pre + '.txt')
