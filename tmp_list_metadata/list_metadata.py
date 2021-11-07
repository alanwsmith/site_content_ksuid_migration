#!/usr/bin/env python3

import frontmatter
import glob
import os

from os.path import isfile


def list_metadata(input_dir):
    files = [
        file for file in glob.glob(f"{input_dir}/*.txt")
        if isfile(file)
    ]

    frontmatter_keys = set()

    for file in files:
        post = frontmatter.load(file)
        for key in post.keys():
            frontmatter_keys.add(key)

        # if 'created' in post:
        #     print(file)
        #     print(f"{post['date']} - {post['created']}")


    for key in sorted(frontmatter_keys):
        print(f"# - [] {key}")

    # print(sorted(frontmatter_keys))


# {'date', 'description', 'created', 'category', 'updated', 'episode', 'thumbnail_full_url', 'title', 'tags', 'originally_posted',
# 'categories', 'thumbnail', 'draft', 'type', 'slub', 'id', 'permalink', 'work_in_progress', 'blurb', 'slug', 'url', 'keywords', 
# 'layout', 'status'}


if __name__ == "__main__":
    input_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/04_status_updates'
    list_metadata(input_dir)



