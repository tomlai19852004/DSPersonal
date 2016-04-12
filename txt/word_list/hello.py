#!/usr/bin/python
import csv
import itertools

writer = open('socialmedia.csv', 'w')
writer.write('order,occurence,word\n')
with open('socialmedia.txt', 'r') as in_file, open('socialmedia.csv', 'wb') as outfile:
    # stripped = (line.strip() for line in in_file)
    # lines = (line for line in stripped if line)
    # grouped = itertools.izip(*[lines] * 3)
    # print grouped
    # with open('architecture.csv', 'w') as out_file:
    #     writer = csv.writer(out_file)
    #     writer.writerow(('order', 'occurence', 'words'))
    #     writer.writerows(grouped)
    txt = csv.reader(in_file, delimiter="	")
    out_csv = csv.writer(outfile)
    out_csv.writerows(txt)
