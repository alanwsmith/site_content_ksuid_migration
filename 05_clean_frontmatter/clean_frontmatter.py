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
            post.metadata.pop('thumbnail')

        if 'thumbnail_full_url' in post:
            post.metadata.pop('thumbnail_full_url')

        if 'layout' in post:
            if 'type' not in post:
                post['type'] = post['layout']
                post.metadata.pop('layout')

        if 'category' in post:
            post['categories'] = [ post['category'] ]
            post.metadata.pop('category')

        if 'draft' in post:
            if post['draft']:
                post['status'] = 'draft'
            post.metadata.pop('draft')

        if 'episode' in post:
            post.metadata.pop('episode')

        if 'keywords' in post:
            post.metadata.pop('keywords')

        if 'layout' in post:
            post.metadata.pop('layout')

        if 'originally_posted' in post:
            post.metadata.pop('originally_posted')

        if 'permalink' in post:
            post.metadata.pop('permalink')

        if 'slub' in post:
            post.metadata.pop('slub')

        if 'tags' in post:
            if len(post['tags']):
                if 'categories' not in post:
                    post['categories'] = []

                for tag in post['tags']:
                    post['categories'].append(tag)
            post.metadata.pop('tags')

        if 'url' in post:
            post.metadata.pop('url')

        if 'work_in_progress' in post:
            post.metadata.pop('work_in_progress')

        # moving eveyrthing to post 
        # there were only a couple other tyings
        post['type'] = 'post'

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
# - [x] draft - use to update status
# - [x] episode - removed
# - [x] id - no change
# - [x] keywords - remove, there aren't many of them
# - [x] layout - removed 
# - [x] originally_posted - removed
# - [x] permalink - removed
# - [x] slub - removed (this was a typo)
# - [x] slug - Keeping through this part of the process
# - [x] status - updating as needed
# - [x] tags
# - [x] thumbnail
# - [x] thumbnail_full_url
# - [x] title - keeping as is for now
# - [x] type - moved the few things that weren't post to be post
# - [x] updated - leaving along for now
# - [x] url - removed 
# - [x] work_in_progress - removed



if __name__ == "__main__":
    input_dir  = '/Users/alans/workshop/site_content_ksuid_migration_data/04_status_updates'
    output_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/05_clean_frontmatter'

    clear_output_dir(output_dir)
    make_files(input_dir, output_dir)


