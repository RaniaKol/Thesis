import os, glob, re
import pandas as pd
from sklearn.model_selection import train_test_split

path = 'final_en/'
list1=[]

for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    
        df = pd.DataFrame(data, columns = ['Text'])
        df['Filename'] = os.path.basename(filename)
        list1.append(df)
df2 = pd.concat(list1, ignore_index=True)
df2.sort_values('Filename',inplace=True)
#df2.to_csv('combined_texts_en.csv', index=False, encoding='utf-8')

train_data, test_valid_data = train_test_split(df2['Text'], test_size=0.2, random_state=42)
test_data, valid_data = train_test_split(test_valid_data, test_size=0.25, random_state=42)

# Write the subsets to separate text files
train_data.to_csv('train_texts_en.txt', index=False, header=None, encoding='utf-8', sep='\t')
test_data.to_csv('test_texts_en.txt', index=False, header=None, encoding='utf-8', sep='\t')
valid_data.to_csv('valid_texts_en.txt', index=False, header=None, encoding='utf-8', sep='\t')