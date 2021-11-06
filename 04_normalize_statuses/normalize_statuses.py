#!/usr/bin/env python3

import frontmatter
import glob
import os

from os.path import isfile


def clear_output_dir(output_dir):
    files_to_delete = [
        file for file in glob.glob(f"{output_dir}/*.txt" )
        if isfile(file)
    ]

    for file_to_delete in files_to_delete:
        os.remove(file_to_delete)

def make_files(input_dir, output_dir):
    files = [
        file for file in glob.glob(f"{input_dir}/*.txt")
        if isfile(file)
    ]

    statuses = set()

    for file in files:
        post = frontmatter.load(file)
        if 'status' not in post:
            post['status'] = 'published'
        elif post['status'] == 'post':
            post['status'] = 'published'


        # if 'status' in post:
        #     print(post['status'])
        #     statuses.add(post['status'])

            # {'post', 'scratch', 'published', 'archive', 'draft', 'wip', 'scratchpad', 'complete'}


        output_path = file.replace(input_dir, output_dir)
        with open(output_path, 'w') as _out_file:
            _out_file.write(frontmatter.dumps(post))


    print('------')
    print(statuses)

if __name__ == "__main__":
    input_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/03_ksuids_added'
    output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/04_status_updates'

    # clear_output_dir(output_dir)
    # make_files(input_dir, output_dir)



