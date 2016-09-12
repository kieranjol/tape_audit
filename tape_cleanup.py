import csv
import sys
import os
from collections import Counter

'''
tape_file = r'C:\Users\kieran.oleary\Documents\audit\tape_dump_working-copy.csv'
temp_file = r'C:\Users\kieran.oleary\Documents\audit\1tape_newlines_removed_lowercase_refs.csv'
film_file = r'C:\Users\kieran.oleary\Documents\audit\film_20160912_working_copy.csv'

read_object = open(tape_file)
reader = csv.reader(read_object)
csv_list = list(reader)

for i in csv_list:
        if '\n' in i[0]:
           i[0] = i[0].replace('\n','').lower()
           
           

with open(temp_file,'w') as fo:
    for i in csv_list:
        if '\n' in i[0]:
            fo.write(str(i[0]))
'''
def clear_newlines():
    tape_file = r'C:\Users\kieran.oleary\Documents\audit\tape_dump_working-copy.csv'
    temp_file = r'C:\Users\kieran.oleary\Documents\audit\1film_newlines_removed_lowercase_refs.csv'
    film_file = r'C:\Users\kieran.oleary\Documents\audit\film_20160912_working_copy.csv'

    read_object = open(film_file)
    reader = csv.reader(read_object)
    csv_list = list(reader)
    
    for i in csv_list:
        f = open(temp_file, 'ab')
        try:
            if '\n' in i[0]:
               i[0] = i[0].replace('\n','').lower()
            else:
               i[0] = i[0].lower()
            writer = csv.writer(f)
            writer.writerow(i)
        finally:
            f.close()
    '''    
    for i in csv_list:
        if '\n' in i[0]:
           i[0] = i[0].replace('\n','').lower()

    with open(temp_file,'w') as fo:
        for i in csv_list:
            if '\n' in i[0]:
                fo.write(str(i[0]))
    '''
    
def unique_tape():
    # this currently shows dupes, nbot exactly sole reference numbers - still a useful audit.
    tape_file = r'C:\Users\kieran.oleary\Documents\audit\1tape_newlines_removed_lowercase_refs.csv'
    temp_file = r'C:\Users\kieran.oleary\Documents\audit\2tape_newlines_removed_lowercase_refs_count.csv'
    film_file = r'C:\Users\kieran.oleary\Documents\audit\film_20160912_working_copy.csv'

    read_object = open(tape_file)
    reader = csv.reader(read_object)
    csv_list = list(reader)
    ref_list = []
    for i in csv_list:
       ref_list.append((i[0], i[1]))
     
    counter_dict =  Counter(ref_list)
    
        
    with open(temp_file, 'w') as fo:
        for i in counter_dict:
            fo.write(str(i[0]) + ', ' + str(i[1]) + ', '+ str(counter_dict[i]) + '\n')
        
   
unique_tape()    
        
        