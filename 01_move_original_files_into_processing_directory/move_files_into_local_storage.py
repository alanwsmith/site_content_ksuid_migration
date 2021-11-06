#!/usr/bin/env python3

import frontmatter
import glob
import re
import os
import os.path
import subprocess
import time
from os.path import isfile
from shutil import copy2

input_dir = "/Users/alans/Dropbox/grimoire"
output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/01_original_files'

files_to_delete = [
    file for file in glob.glob(
        f"{output_dir}/*.txt"
    )
    if isfile(file)
]

for file_to_delete in files_to_delete:
    os.remove(file_to_delete)

input_files = [
    file for file in glob.glob(
        f"{input_dir}/*.txt"
    )
    if isfile(file)
]


def copy_file_keeping_creation_date(src_path, output_path):
    # TODO: Add error handling in all this?
    creation_time = subprocess.run(['stat', '-f', '%B', src_path], stdout=subprocess.PIPE).stdout.decode('utf-8')
    date_string = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(int(creation_time)))
    copy2(src_path, output_path)
    response = subprocess.run(['SetFile', '-d', date_string, output_path]) 
    print(response)

for file in input_files:
    print(f'---------------------------------------')
    print(f"Working on: {file}")
    post = frontmatter.load(file)
    if 'title' in post:
        print(f"-- {post['title']}")
        output_path = file.replace(input_dir, output_dir) 
        copy_file_keeping_creation_date(file, output_path)
    else:
        print("-- skipping")

print("Process complete")

