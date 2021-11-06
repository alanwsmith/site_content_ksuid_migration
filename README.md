# site_content_ksuid_migration

This is the set of movers that updates the mdx file's frontmatter. And gets
all the KSUID stuff in place for the URLS

Should only need to run this process one time.

TODO:

- [x] Get list of initial slugs to use for redirects
- [x] Move files working directory with original dates
- [] Normalize dates to ISO8601 w/o timezones in frontmatter
- [] Set status to `unpublished` for files with slug of `/tbd`

OTHER:

- [] Make sure titles are all on one line
- [] Add `updated` timestamps to all files
- [] Translate titles to file names then remove titles
- [] Remove `created` time stamps
-
