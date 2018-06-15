#!/usr/bin/python
# -*- coding:utf-8 -*-
import codecs
import argparse
import io

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('utf8_file', help="utf8 file to be converted to shift jis")
    parser.add_argument('shiftjis_file', help="Output file name converted to shift jis")
    args = parser.parse_args()
    # Shift_JIS ファイルのパス
    shiftjis_csv_path = args.shiftjis_file
    # UTF-8 ファイルのパス
    utf8_csv_path = args.utf8_file

    # 文字コードを utf-8 に変換して保存
    with io.open(utf8_csv_path, mode='r', encoding='utf-8') as input_file:
        with io.open(shiftjis_csv_path, mode='w', encoding='shift_jis') as output:
            for row in input_file:
                print(row)
                output.write(row)

if __name__ == '__main__':
    main()
