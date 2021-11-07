#!/usr/bin/env python3

import difflib
import clean_frontmatter
import unittest
import filecmp
import sys
import io

from pathlib import Path

class TestNormalizeDates(unittest.TestCase):

    def test_first_file(self):

        input_dir = "data_for_tests/input"
        output_dir = "data_for_tests/output"
        target_dir = "data_for_tests/targets"

        clean_frontmatter.clear_output_dir(
            output_dir
        )

        clean_frontmatter.make_files(
            input_dir=input_dir,
            output_dir=output_dir
        )

        # make sure files with no content don't get moved
        self.assertFalse(
            Path('data_for_tests/output/0.txt').is_file()
        )

        file_list = ['1', '2', '3', '4', '5']

        for file in file_list:
            a_file = f"{output_dir}/{file}.txt"
            b_file = f"{target_dir}/{file}.txt"
            with open(a_file) as _a:
                a_list = _a.read().splitlines()
            with open(b_file) as _b:
                b_list = _b.read().splitlines()
            self.assertListEqual(
                a_list, b_list
            )


if __name__ == "__main__":
    unittest.main()

