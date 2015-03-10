#!/usr/bin/env python

import re
import optparse


def parse_git_md(md_filename, md_add_toc=False):
    toc = []            # Each entry is one line of TOC
    with open(md_filename) as file:
        content = file.readlines()
        for line in content:
            m = re.search('^([#]{1,6}) (.*)$', line)
            if m is not None and m.groups():
                header = m.group(1)
                hx = len(header)    # if h1, h2, h3, h4...
                # print m.groups(), hx, header
                header_text = m.group(2)
                header_mangled = re.sub("[^a-zA-Z0-9 ]", "", header_text).replace(' ','-').lower()
                toc_line = "  " * hx + "* [%s](#%s)"% (header_text, header_mangled.lower())
                toc.append(toc_line)
                print toc_line


def main():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
                      dest='md_filename',
                      metavar="FILE",
                      help='Which MD file to open')

    parser.add_option('-a', '--add',
                      dest='md_add_toc',
                      metavar=False,
                      action="store_true",
                      help='Adds TOC inside MD file')

    (opts, args) = parser.parse_args()

    if opts.md_filename:
        parse_git_md(opts.md_filename, md_add_toc=opts.md_add_toc)

if __name__ == '__main__':
    main()
