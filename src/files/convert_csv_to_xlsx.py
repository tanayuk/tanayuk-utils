#!/usr/bin/env python
# -*- coding:utf-8 -*-
import codecs
import argparse
import io
import glob
import csv
from xlsxwriter.workbook import Workbook

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', help="csv file name")
    args = parser.parse_args()
    csv_file_path = args.csv_file
    workbook = Workbook(csv_file_path[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csv_file_path, 'rt', encoding='utf-8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r,c,col)
    workbook.close()

if __name__ == '__main__':
    main()
