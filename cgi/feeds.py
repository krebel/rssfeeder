#!/usr/bin/env python
#!/usr/bin/python

import feedparser, os, sys, cgi, cgitb
reload(sys)
sys.setdefaultencoding('utf-8')

cgitb.enable()

print "Content-type: text/html\n\n"

##***NOTE!!: After adding the 5 lines above, stopped getting the 'UnicodeEncodeError: 'ascii' codec can't encode character u'\xfc' in position 9: ordinal not in range(128)'


# Empty the output files prior to adding new content:
bbcout = open('/var/www/html/bbc.html', 'w')
rtrzout = open('/var/www/html/rtrz.html', 'w')
wsjout = open('/var/www/html/wsj.html', 'w')
slshout = open('/var/www/html/slsh.html', 'w')
zout = open('/var/www/html/z.html', 'w')
schnout = open('/var/www/html/schn.html', 'w')
krebsout = open('/var/www/html/krebs.html', 'w')
ieeeout = open('/var/www/html/ieee.html', 'w')

outFilez = (bbcout, rtrzout, wsjout, schnout, slshout, zout, krebsout)

for word in outFilez:
    word.write('')
    word.close()



# Open files for append:
bbcout = open('/var/www/html/bbc.html', 'a')
rtrzout = open('/var/www/html/rtrz.html', 'a')
wsjout = open('/var/www/html/wsj.html', 'a')
slshout = open('/var/www/html/slsh.html', 'a')
zout = open('/var/www/html/z.html', 'a')
schnout = open('/var/www/html/schn.html', 'a')
krebsout = open('/var/www/html/krebs.html', 'a')
ieeeout = open('/var/www/html/ieee.html', 'a')



###### Feeds:
btn = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
bwrld = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
bbiz = feedparser.parse('http://feeds.bbci.co.uk/news/business/rss.xml')
bsci = feedparser.parse('http://feeds.bbci.co.uk/news/science_and_environment/rss.xml')
btech = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml')
rtrzbiz = feedparser.parse('http://feeds.reuters.com/reuters/businessNews')
rtrzmost = feedparser.parse('http://feeds.reuters.com/reuters/MostRead')
rtrz3 = feedparser.parse('http://feeds.reuters.com/news/artsculture')
rtrz5 = feedparser.parse('http://feeds.reuters.com/reuters/companyNews')
rtrz7 = feedparser.parse('http://feeds.reuters.com/reuters/environment')
rtrz8 = feedparser.parse('http://feeds.reuters.com/reuters/healthNews')
rtrz9 = feedparser.parse('http://feeds.reuters.com/reuters/lifestyle')
rtrz10 = feedparser.parse('http://feeds.reuters.com/news/reutersmedia')
rtrz11 = feedparser.parse('http://feeds.reuters.com/news/wealth')
rtrz12 = feedparser.parse('http://feeds.reuters.com/news/artsculture')
rtrz21 = feedparser.parse('http://feeds.reuters.com/reuters/oddlyEnoughNews')
rtrz22 = feedparser.parse('http://feeds.reuters.com/ReutersPictures')
rtrz23 = feedparser.parse('http://feeds.reuters.com/reuters/peopleNews')
rtrz24 = feedparser.parse('http://feeds.reuters.com/Reuters/PoliticsNews')
rtrz25 = feedparser.parse('http://feeds.reuters.com/reuters/scienceNews')
rtrz27 = feedparser.parse('http://feeds.reuters.com/reuters/technologyNews')
rtrz28 = feedparser.parse('http://feeds.reuters.com/reuters/topNews')
rtrz29 = feedparser.parse('http://feeds.reuters.com/Reuters/domesticNews')
rtrz30 = feedparser.parse('http://feeds.reuters.com/Reuters/worldNews')
rtrz31 = feedparser.parse('http://feeds.reuters.com/reuters/bankruptcyNews')
rtrz32 = feedparser.parse('http://feeds.reuters.com/reuters/bondsNews')
rtrz33 = feedparser.parse('http://feeds.reuters.com/news/deals')
rtrz34 = feedparser.parse('http://feeds.reuters.com/news/economy')
rtrz35 = feedparser.parse('http://feeds.reuters.com/reuters/globalmarketsNews')
rtrz36 = feedparser.parse('http://feeds.reuters.com/news/hedgefunds')
rtrz37 = feedparser.parse('http://feeds.reuters.com/reuters/hotStocksNews')
rtrz38 = feedparser.parse('http://www.reuters.com/rssFeed/newIssuesNews')
rtrz39 = feedparser.parse('http://feeds.reuters.com/reuters/mergersNews')
rtrz40 = feedparser.parse('http://feeds.reuters.com/reuters/governmentfilingsNews')
rtrz41 = feedparser.parse('http://feeds.reuters.com/reuters/summitNews')
rtrz42 = feedparser.parse('http://feeds.reuters.com/reuters/USdollarreportNews')
rtrz43 = feedparser.parse('http://feeds.reuters.com/news/usmarkets')
rtrz44 = feedparser.parse('http://feeds.reuters.com/reuters/basicmaterialsNews')
rtrz45 = feedparser.parse('http://feeds.reuters.com/reuters/cyclicalconsumergoodsNews')
rtrz46 = feedparser.parse('http://feeds.reuters.com/reuters/USenergyNews')
rtrz48 = feedparser.parse('http://feeds.reuters.com/reuters/financialsNews')
rtrz49 = feedparser.parse('http://feeds.reuters.com/reuters/UShealthcareNews')
rtrz50 = feedparser.parse('http://feeds.reuters.com/reuters/industrialsNews')
rtrz51 = feedparser.parse('http://feeds.reuters.com/reuters/USmediaDiversifiedNews')
rtrz52 = feedparser.parse('http://feeds.reuters.com/reuters/noncyclicalconsumergoodsNews')
rtrz53 = feedparser.parse('http://feeds.reuters.com/reuters/technologysectorNews')
rtrz54 = feedparser.parse('http://feeds.reuters.com/reuters/utilitiesNews')
rtrz55 = feedparser.parse('http://feeds.feedburner.com/reuters/blogs/data-dive')
rtrz56 = feedparser.parse('http://feeds.feedburner.com/reuters/blogs/DavosNotebook')
rtrz57 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/FinancialRegulatoryForum')
rtrz58 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/GlobalInvesting')
rtrz59 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/HugoDixon')
rtrz60 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/India')
rtrz61 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/JamesSaft')
rtrz62 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/macroscope')
rtrz63 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/mediafile')
rtrz64 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/newsmaker')
rtrz65 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/photo')
rtrz66 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/SummitNotebook')
rtrz67 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/talesfromthetrail')
rtrz68 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/the-great-debate')
rtrz69 = feedparser.parse('http://feeds.reuters.com/reuters/blogs/the-human-impact')
rtrz70 = feedparser.parse('http://feeds.reuters.com/UnstructuredFinance')
wsjPg1 = feedparser.parse('http://www.wsj.com/xml/rss/3_7205.xml')
wsjMost = feedparser.parse('http://www.wsj.com/xml/rss/3_7198.xml')
wsjHomeUS = feedparser.parse('http://www.wsj.com/xml/rss/3_7011.xml')
wsjWorld = feedparser.parse('http://www.wsj.com/xml/rss/3_7085.xml')
wsjUsbiz = feedparser.parse('http://www.wsj.com/xml/rss/3_7014.xml')
wsjTech = feedparser.parse('http://www.wsj.com/xml/rss/3_7455.xml')
wsjPersTech = feedparser.parse('http://www.wsj.com/xml/rss/3_7454.xml')
slsh = feedparser.parse('http://rss.slashdot.org/Slashdot/slashdotMain')
z = feedparser.parse('http://www.zerohedge.com/fullrss2.xml')
schn = feedparser.parse('https://www.schneier.com/blog/atom.xml')
krebs = feedparser.parse('http://krebsonsecurity.com/feed/')
ieee = feedparser.parse('http://spectrum.ieee.org/rss/fulltext')



#################### Write the files ####################

##### BBC:

# BBC Top News:
bbcout.write("<H1>" + btn['feed']['title'] + "</H1>" + "\n\n")
#print btn['feed']['link']
#print btn['entries'][0]['title']
for post in btn.entries:
   # print post.title  + ": " + post.link + "\n"
    bbcout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" + "\n")
bbcout.write("<br>")

bbcout.write("<H1>" + bwrld['feed']['title'] + "</H1>" + "\n\n")
for post in bwrld.entries:
    bbcout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" + "\n")
bbcout.write("<br>")


bbcout.write("<H1>" + bbiz['feed']['title'] + "</H1>" + "\n\n")
for post in bbiz.entries:
    bbcout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" + "\n")
bbcout.write("<br>")

bbcout.write("<H1>" + bsci['feed']['title'] + "</H1>" + "\n\n")
for post in bsci.entries:
    bbcout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" + "\n")
bbcout.write("<br>")

bbcout.write("<H1>" + btech['feed']['title'] + "</H1>" + "\n\n")
for post in btech.entries:
    bbcout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" + "\n")
bbcout.write("<br>")

bbcout.close()



##### WSJ

wsjout.write("<H2>Wall Street Journal</H2><br><br>")
wsjout.write("<H1>" + wsjPg1['feed']['title'] + "</H1>" + "\n\n")
for post in wsjPg1.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.write("<H1>" + wsjMost['feed']['title'] + "</H1>" + "\n\n")
for post in wsjMost.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.write("<H1>" + wsjHomeUS['feed']['title'] + "</H1>" + "\n\n")
for post in wsjHomeUS.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.write("<H1>" + wsjWorld['feed']['title'] + "</H1>" + "\n\n")
for post in wsjWorld.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.write("<H1>" + wsjUsbiz['feed']['title'] + "</H1>" + "\n\n")
for post in wsjUsbiz.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.write("<H1>" + wsjTech['feed']['title'] + "</H1>" + "\n\n")
for post in wsjTech.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.write("<H1>" + wsjPersTech['feed']['title'] + "</H1>" + "\n\n")
for post in wsjPersTech.entries:
    wsjout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

wsjout.close()



#####Schneier on Security:

schnout.write("<H1>" + schn['feed']['title'] + "</H1>" + "\n\n")
for post in schn.entries:
    schnout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

schnout.close()




##### Slashdot:

slshout.write("<H1>" + slsh['feed']['title'] + "</H1>" + "\n\n")
for post in slsh.entries:
    slshout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

slshout.close()



##### Zerohedge:

zout.write("<H1>ZH</H1><br>")
for post in z.entries:
    zout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

zout.close()



##### Krebs on Security:

krebsout.write("<H1>Krebs on Security</H1><br>")
for post in krebs.entries:
    krebsout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

krebsout.close()



##### IEE:

ieeeout.write("<H1>IEEE Spectrum</H1><br>")
for post in ieee.entries:
    ieeeout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

ieeeout.close()




##### Reuters

reuters = (rtrzbiz, rtrzmost, rtrz3, rtrz5, rtrz7, rtrz8, rtrz9, rtrz10, rtrz11, rtrz12, rtrz21, rtrz22, rtrz23, rtrz24, rtrz25, rtrz27, rtrz28, rtrz29, rtrz30, rtrz31, rtrz32, rtrz33, rtrz34, rtrz35, rtrz36, rtrz37, rtrz38, rtrz39, rtrz40, rtrz41, rtrz42, rtrz43, rtrz44, rtrz45, rtrz46, rtrz48, rtrz49, rtrz50, rtrz51, rtrz52, rtrz53, rtrz54, rtrz55, rtrz56, rtrz57, rtrz58, rtrz59, rtrz60, rtrz61, rtrz62, rtrz63, rtrz64, rtrz65, rtrz66, rtrz67, rtrz68, rtrz69, rtrz70)

for word in reuters:
    rtrzout.write("<H1>" + word['feed']['title'] + "</H1>" + "\n\n")
    for post in word.entries:
        rtrzout.write("<a href='" + post.link + "'>" + post.title + "</a>" + "<br>" +  "\n")

rtrzout.close()



#print os.environ['HTTP_REFERER']
print('<p>Refresh complete</p>')

