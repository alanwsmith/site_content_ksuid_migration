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

    for file in files:
        print(file)
        post = frontmatter.load(file)
        if 'status' not in post:
            post['status'] = 'published'
        elif post['status'] == 'complete':
            post['status'] = 'published'
        elif post['status'] == 'post':
            post['status'] = 'published'
        elif post['status'] == 'wip':
            post['status'] = 'scratch'
        elif post['status'] == 'scratchpad':
            post['status'] = 'scratch'

        if 'slug' in post:
            if post['slug'] == '/tbd':
                post['status'] = 'unpublished'

        # x N/A = 'published'
        # x 'post' = 'published'
        # ok 'scratch'
        # ok 'published'
        # ok 'archive'
        # ok 'draft'
        # x 'wip' = 'scratch'
        # x 'scratchpad' = 'scratch'
        # x 'complete' = 'published'
        # x slug /tbd = unpublished 


        output_path = file.replace(input_dir, output_dir)
        with open(output_path, 'w') as _out_file:
            _out_file.write(frontmatter.dumps(post))


if __name__ == "__main__":
    input_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/03_ksuids_added'
    output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/04_status_updates'

    clear_output_dir(output_dir)
    make_files(input_dir, output_dir)



