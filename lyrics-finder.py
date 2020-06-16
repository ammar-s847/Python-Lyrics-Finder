import requests

def getHtmlCode(url): # Returns all the html code from the URL
	r = requests.get(url)
	return r.text

def searchSong(queryString):
    htmlCode = getHtmlCode(queryString)
    startIndex = '''class="text-left visitedlyr" onclick="javascript:document.location.href='''
    link = htmlCode[htmlCode.index(startIndex) + len(startIndex) + 1 : htmlCode.index('''" style="cursor''') - 1]
    return link

def getLyrics(link):
    htmlCode = getHtmlCode(link)
    startIndex = htmlCode.index("<div>", htmlCode.index("<span id=\"cf_text_top\"></span>")) + 5 # + len(str(<span id="cf_text_top"></span>)) + 
    lyrics = htmlCode[startIndex : htmlCode.index("</div>", startIndex)]
    lyrics = lyrics.replace("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->", "")
    lyrics = lyrics.replace("&quot;", "\"")
    return lyrics.replace("<br><br>", "\n").replace("<br>", "\n")

song = input("Enter a Song name and optionally, the Artist name: ")
try:
    print("Lyrics for \"" + song + "\"")
    queryString = str("https://search.azlyrics.com/search.php?q=" + song).replace(" ", "+")
    print("Extracted from " + searchSong(queryString))
    print(getLyrics(searchSong(queryString)))
except:
    print("An error occured")