#!/usr/bin/env python3

import datetime
import frontmatter
import glob
import os
import re
import time

from os.path import isfile
from dateutil.parser import parse


def clear_output_dir(output_dir):
    files_to_delete = [
        file for file in glob.glob(f"{output_dir}/*.txt" )
        if isfile(file)
    ]

    for file_to_delete in files_to_delete:
        os.remove(file_to_delete)

def make_files(input_dir, output_dir):
    input_files = [
        file for file in glob.glob(f"{input_dir}/*.txt")
        if isfile(file)
    ]

    for file in input_files:
        print(f'---------------------------------------')
        print(f"Working on: {file}")
        post = frontmatter.load(file)
        if 'date' not in post:
            print("Found problem file:")
            print(file)
            import sys
            sys.exit()
        else:
            dest_file = file.replace(input_dir, output_dir)
            new_date_time = ""

            if isinstance(post['date'], int):
                post['date'] = time.strftime(
                    '%Y-%m-%dT%H:%M:%S',
                    time.localtime(int(post['date']))
                )
            elif isinstance(post['date'], datetime.date):
                post['date'] = post['date'].strftime(
                    '%Y-%m-%dT%H:%M:%S'
                )
            else:
                new_date_time = parse(post['date'])
                post['date'] = new_date_time.strftime("%Y-%m-%dT%H:%M:%S")

            with open(dest_file, 'w') as _out_file:
                _out_file.write(frontmatter.dumps(post))

    #         if isinstance(post['date'], datetime.date):
    #             new_date_time = post['date']
    #         else:
    #             pattern = re.compile(r'^\d\d\d\d\d\d\d\d\d\d')
    #             if pattern.search(str(post['date'])):
    #                 datetime_string = time.strftime(
    #                     '%Y-%m-%dT%H:%M:%S-0400',
    #                     time.localtime(int(post['date']))
    #                 )
    #                 new_date_time = parse(datetime_string)
    #             else:


if __name__ == "__main__":

    input_dir= '/Users/alans/workshop/site_ksuid_migration/data_files/01_original_files'
    output_dir = '/Users/alans/workshop/site_ksuid_migration/data_files/02_normalized_dates'

    # clear_output_dir(output_dir)
    # make_files(input_dir, output_dir)
