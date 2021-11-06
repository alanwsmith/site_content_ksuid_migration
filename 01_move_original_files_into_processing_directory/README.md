This is the first part of the process that
pulls in files from the grimoire. 

It pulls in files that have frontmatter
and a title in that frontmatter. 

The assumption is that that'll hit all 
the main files. It's more that is 
currently pulled by the live process
which works off a slug, but that's expected
and desired. The goal will be to use the 
title's (and, actually the file names) 
to auto generate the slug. 

When the files are moved a specific process
makes sure to copy their origina "birth" 
timestamp as well. This will be used 
for adding and normalizing dates where
needed. 


