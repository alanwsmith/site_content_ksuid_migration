# site_content_ksuid_migration

This is the set of movers that updates the mdx file's frontmatter. And gets
all the KSUID stuff in place for the URLS

Should only need to run this process one time.

TODO:

- [x] Get list of initial slugs to use for redirects
- [] Move files working directory with original dates TODO: ensure modidifed time is accurate to use for updates
- [x] Normalize dates to ISO8601 w/o timezones in frontmatter
- [] Set statuses to: unpublished, scratch, draft, published (all slug: /tbd to unpublished)
- [] Add status to all posts (gotta figure out the logic) - can probably base it off date.
- [] Generate list of initial slug and filenames to the corresponding KSUIDs

OTHER:

- [] Convert 'description' frontmatter to 'blurb'
- [] Make sure titles are all on one line
- [] Add `updated` timestamps to all files
- [] Translate titles to file names then remove titles
- [] Remove `created` time stamps
- [] Figure out what to do about tags (i.e. maybe rename to keywords? or, maybe not?)
- [] Verify all posts have minimum set of: blurb, category, date, id, tags, type, updated
- [] Clean up categories
- [] Clean up tags
