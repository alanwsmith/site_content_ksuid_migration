# site_content_ksuid_migration

This is the set of movers that updates the mdx file's frontmatter. And gets
all the KSUID stuff in place for the URLS

Should only need to run this process one time.

TODO:

- [x] Get list of initial slugs to use for redirects
- [] Move files working directory with original dates TODO: ensure modidifed time is accurate to use for updates
- [] Add `updated` timestamps to all files
- [x] Normalize dates to ISO8601 w/o timezones in frontmatter
- [x] Set statuses to: archive, unpublished, scratch, draft, published (all slug: /tbd to unpublished)
- [x] Add status to all posts (gotta figure out the logic) - can probably base it off date.
- [x] Generate list of initial slug and filenames to the corresponding KSUIDs

OTHER:

- [] Add `categories` when missing.
- [x] Convert 'description' frontmatter to 'blurb'
- [] Translate titles to file names then remove titles
- [x] Remove `created` time stamps
- [] Figure out what to do about tags (i.e. maybe rename to keywords? or, maybe not?)
- [] Verify all posts have minimum set of: blurb, categories, date, id, type, updated
- [] Clean up categories (i.e. review and remove any that don't make sense)
- [] Clean up tags (i.e. review and remove any that don't make sense - and colapse into categoreis)
- [] Look at `title: null` in `py- Delete A Key From A Dictionary.txt`
- [] Don't output posts with no content
-
-
