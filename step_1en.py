import os, glob, re
from bs4 import BeautifulSoup

path = 'en/'
dest_path = 'english1/'
for filename in glob.glob(os.path.join(path, '*.xml')):
   
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
      cleaner_filename = filename.replace("en/", "")
      filename_destination = dest_path + cleaner_filename
      file2 = open(filename_destination,'w')
      data = f.read()
      soup = BeautifulSoup(data, 'xml')
      body = soup.find('body')

      clean = re.sub('\n', 'XYZ', str(body))
      p2get = re.compile(r'<!(.*?)->')
      removed_stuff = re.sub(p2get, '', clean)
      result = re.sub('XYZ', '\n', removed_stuff)
      
      clean = re.sub('\n', 'XYZ', result)
      p2get = re.compile(r'<note(.*?)</note>')
      removed_stuff = re.sub(p2get, '', clean)
      result = re.sub('XYZ', '\n', removed_stuff)
      
      clean = re.sub('\n', 'XYZ', result)
      p2get = re.compile(r'<bibl(.*?)</bibl>')
      removed_stuff = re.sub(p2get, '', clean)
      result = re.sub('XYZ', '\n', removed_stuff)
      
      clean = re.sub('\n', 'XYZ', result)
      p2get = re.compile(r'<bibl>(.*?)</bibl>')
      removed_stuff = re.sub(p2get, '', clean)
      result = re.sub('XYZ', '\n', removed_stuff)

      clean = re.sub('\n', 'XYZ', result)
      p2get = re.compile(r'<reg>(.*?)</reg>')
      removed_stuff = re.sub(p2get, '', clean)
      result = re.sub('XYZ', '\n', removed_stuff)

      file2.write(result)
   pre, ext = os.path.splitext(filename_destination)
   os.rename(filename_destination, pre + '.xml')


   
