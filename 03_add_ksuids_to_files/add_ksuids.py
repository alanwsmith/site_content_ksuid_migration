#!/usr/bin/env python3

import frontmatter
import glob
import os
import subprocess
import time

from os.path import isfile

# This is the one that adds KSUIDs. 
# It sorts all the files based off the date in the 
# frontmatter than creates a KSUID for each one in order
# waiting a second between so the dates order up
# The dates aren't accurate to the posts, but that's fine
# 

def clear_output_dir(output_dir):
    files_to_delete = [
        file for file in glob.glob(f"{output_dir}/*.txt" )
        if isfile(file)
    ]

    for file_to_delete in files_to_delete:
        os.remove(file_to_delete)

def generate_files(input_dir, output_dir):
    files = {}
    source_files = [
        file for file in glob.glob(f"{input_dir}/*.txt")
        if isfile(file)
    ]

    for file in source_files:
        post = frontmatter.load(file)
        post_date = post['date']
        if post_date not in files:
            files[post_date] = []
        files[post_date].append(file)

    for the_time in sorted(files):
        # print(the_time)
        for file in files[the_time]:
            print(file)
            post = frontmatter.load(file)
            ksuid_string = subprocess.run(['ksuid'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            ksuid_short = ksuid_string[0:12]
            post['id'] = ksuid_short
            output_path = file.replace(input_dir, output_dir)
            with open(output_path, 'w') as _out_file:
                _out_file.write(frontmatter.dumps(post))
            time.sleep(1)


if __name__ == "__main__":

    input_dir  = '/Users/alans/workshop/site_content_ksuid_migration_data/02_normalized_dates'
    output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/03_ksuids_added'

    clear_output_dir(output_dir)
    generate_files(input_dir, output_dir)



