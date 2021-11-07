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
        post = frontmatter.load(file)

        # delete 'created' if it exists
        if 'created' in post:
            post.metadata.pop('created')

        if 'description' in post:
            if post['description'] == None:
                post.metadata.pop('description')

        if 'thumbnail' in post:
            if post['thumbnail'] == None:
                post.metadata.pop('thumbnail')



        output_file = file.replace(input_dir, output_dir)
        with open(output_file, 'w') as _out:
            frontmatter.dump(post, output_file)



# {'date', 'description', 'created', 'category', 'updated', 'episode', 'thumbnail_full_url', 'title', 'tags', 'originally_posted',
# 'categories', 'thumbnail', 'draft', 'type', 'slub', 'id', 'permalink', 'work_in_progress', 'blurb', 'slug', 'url', 'keywords', 
# 'layout', 'status'}




if __name__ == "__main__":
    input_dir  = '/Users/alans/workshop/site_content_ksuid_migration_data/04_status_updates'
    output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/05_clean_frontmatter'

    # clear_output_dir(output_dir)
    # make_files(input_dir, output_dir)



