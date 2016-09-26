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
    # this currently shows dupes, not exactly sole reference numbers - still a useful audit.
    tape_file = r'C:\Users\kieran.oleary\Documents\audit\1tape_newlines_removed_lowercase_refs.csv'
    temp_file = r'C:\Users\kieran.oleary\Documents\audit\20160926_2tape_newlines_removed_lowercase_refs_count_csvmodule.csv'
    film_file = r'C:\Users\kieran.oleary\Documents\audit\film_20160912_working_copy.csv'
    read_object = open(tape_file)
    reader = csv.reader(read_object)
    csv_list = list(reader)
    ref_list = []
    for i in csv_list:
       ref_list.append((i[0], i[1]))
    counter_dict =  Counter(ref_list) 
    with open(temp_file, 'ab') as fo:
        for i in counter_dict:
            writer = csv.writer(fo)
            row = (str(i[0]), str(i[1]), str(counter_dict[i]))
            if counter_dict[i] > 1:
                writer.writerow(row)
def unique_tape_refs():
    # this currently shows dupes, not exactly sole reference numbers - still a useful audit.
    tape_file = r'C:\Users\kieran.oleary\Documents\audit\1tape_newlines_removed_lowercase_refs.csv'
    temp_file = r'C:\Users\kieran.oleary\Documents\audit\20160926_single_tape_may_be_film_holdings.csv'
    film_file = r'C:\Users\kieran.oleary\Documents\audit\film_20160912_working_copy.csv'
    read_object = open(tape_file)
    reader = csv.reader(read_object)
    csv_list = list(reader)
    ref_list = []
    for i in csv_list:
       ref_list.append(i[0])
    counter_dict =  Counter(ref_list)    
    with open(temp_file, 'ab') as fo:
        for i in counter_dict:
            writer = csv.writer(fo)
            row = (str(i), str(counter_dict[i]))
            if counter_dict[i] == 1:
                writer.writerow(row)      
def check_if_unique_tapes_have_film_holdings():
    tape_file = r'C:\Users\kieran.oleary\Documents\audit\20160926_single_tape_may_be_film_holdings.csv'
    temp_file = r'C:\Users\kieran.oleary\Documents\audit\20160926_real_sole_tapes.csv'
    film_file = r'C:\Users\kieran.oleary\Documents\audit\1film_newlines_removed_lowercase_refs.csv'
    read_object = open(tape_file)
    reader = csv.reader(read_object)
    tape_csv_list = list(reader)
    film_read_object = open(film_file)
    film_reader = csv.reader(film_read_object)
    film_csv_list = list(film_reader)
    just_film_ref_numbers = []
    for i in film_csv_list:
        just_film_ref_numbers.append(i[0])
    with open(temp_file, 'ab') as fo:
        writer = csv.writer(fo)
        for records in tape_csv_list:
                    if records[0] not in just_film_ref_numbers:
                        writer.writerow([records[0]])
 
        