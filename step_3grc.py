import os, glob, re
from bs4 import BeautifulSoup

path = 'greek2/'
dest_path = 'greek3/'
for filename in glob.glob(os.path.join(path, '*.xml')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
      cleaner_filename = filename.replace("greek2/", "")
      filename_destination = dest_path + cleaner_filename
      file2 = open(filename_destination,'w')
      data = f.read()
      soup = BeautifulSoup(data, 'xml')
      for i in soup.findAll(text=True):
         file2.write(i)
   pre, ext = os.path.splitext(filename_destination)
   os.rename(filename_destination, pre + '.txt')