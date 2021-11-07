#!/usr/bin/env python3 

import frontmatter
import glob
import json

from os.path import isfile


def make_map(input_dir, output_file):
    input_files = [
        file for file in glob.glob(f"{input_dir}/*.txt")
        if isfile(file)
    ]

    data = { "pages": [] }

    for file in input_files:
        post = frontmatter.load(file)
        if 'slug' in post:
            file_data = {
                'id': post['id'],
                'slug': post['slug'],
                'filename': file.split('/')[-1]
            }
            data['pages'].append(file_data)

    with open(output_file, 'w') as _out:
        json.dump(data, _out, sort_keys=True, indent=2)

if __name__ == "__main__":
    input_dir = '/Users/alans/workshop/site_content_ksuid_migration_data/03_ksuids_added'
    output_file = '/Users/alans/workshop/site_content_ksuid_migration_data/03b_slug_to_ksuid_map/slug_to_ksuid_map.json'
    make_map(input_dir, output_file)


