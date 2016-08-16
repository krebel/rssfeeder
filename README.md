# rssfeeder
python cgi script 'feeds.py' queries some newsy sites' rss links to populate local html pages with headlines
  Assuming a Linux based apache/cgi:
- feeds.py lives in /usr/lib/cgi-bin 
- index.html, *.htm and iframepage.html live in /var/www/html

TODO:
- fix the ugly python script error at end of execution which started after adding a ton more news sites to query from (which oddly enough doesn't prevent the intended functionality from working)
- add some jquery to provide proper status feedback when waiting on the refresh button (this broke after adding a ton more queries)
- add more sites
- cleanup code to shorten and beautify
- work on performance...currently takes about 2 minutes or slightly less to complete a refresh of rss query/links
- change look/feel, currently hyperlink styles look simplistic/dated/default
