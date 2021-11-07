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
            else:
                post['blurb'] = post['description']
                post.metadata.pop('description')

        if 'thumbnail' in post:
            if post['thumbnail'] == None:
                post.metadata.pop('thumbnail')

        if 'layout' in post:
            if 'type' not in post:
                post['type'] = post['layout']
                post.metadata.pop('layout')

        if 'category' in post:
            post['categories'] = [ post['category'] ]
            post.metadata.pop('category')


        # if 'draft' in post:
        #     print(file)
        #     print(post['draft'])

        # Only output if there is content
        if post.content:
            output_file = file.replace(input_dir, output_dir)
            with open(output_file, 'w') as _out:
                frontmatter.dump(post, output_file)


# - [x] blurb - no change
# - [x] categories - no change
# - [x] category - convert to categories 
# - [x] created - delete
# - [x] date - no change
# - [x] description - switch to blurb
# - [] draft
# - [] episode
# - [] id
# - [] keywords
# - [] layout
# - [] originally_posted
# - [] permalink
# - [] slub
# - [] slug
# - [] status
# - [] tags
# - [] thumbnail
# - [] thumbnail_full_url
# - [] title
# - [] type
# - [] updated
# - [] url
# - [] work_in_progress



if __name__ == "__main__":
    input_dir  = '/Users/alans/workshop/site_content_ksuid_migration_data/04_status_updates'
    output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/05_clean_frontmatter'

    clear_output_dir(output_dir)
    make_files(input_dir, output_dir)



