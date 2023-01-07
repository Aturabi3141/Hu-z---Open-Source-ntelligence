import requests
from requests.exceptions import HTTPError

username = input("Kullanıcı adı giriniz: ")
def url(urlgir):   
    url = requests.get(urlgir,"/{}".format(username))
    if (url.status_code == 404): 
        print(urlgir, "Sitesinde","{}Adlı Kullanıcı Bulunamadı!".format(username))
    else:
        print(urlgir,"Sitesinde","{} Adlı Kullanıcı Bulundu".format(username))    
    

url("https://www.yandex.com/{}".format(username))
url(" http://www.yahoo.com/{}".format(username))
url(" http://www.google.com/{}".format(username))
url(" http://www.ask.com/{}".format(username))
url(" http://www.bing.com/{}".format(username))
url(" https://duckduckgo.com/{}".format(username))
url(" https://www.topmarks.com/{}".format(username))
url(" http://www.tumblr.com/search/{}".format(username))
url(" https://www.shodan.io/{}".format(username))
url(" https://www.zoomeye.org/{}".format(username))
url(" http://globalfilesearch.com/{}".format(username))
url(" http://www.mmnt.ru/{}".format(username))
url(" http://www.findsimilarsites.com/{}".format(username))
url(" http://www.similarsitesearch.com/{}".format(username))
url(" http://search.aol.com/{}".format(username))
url(" http://www.baidu.com/{}".format(username))
url("https://www.entireweb.com{}".format(username))
url(" http://gigablast.com/{}".format(username))
url(" http://www.goodsearch.com/{}".format(username))
url(" http://www.lycos.com/{}".format(username))
url(" http://home.mywebsearch.com/{}".format(username))
url(" http://www.surfcanyon.com/{}".format(username))
url(" http://www.teoma.com/{}".format(username))
url(" http://www.wolframalpha.com/{}".format(username))  
url(" http://all-io.net/{}".format(username))
url(" http://www.infospace.com/{}".format(username))
url(" http://www.instya.com/{}".format(username))
url(" http://www.izito.com/{}".format(username))
url(" http://www.monstercrawler.com/{}".format(username))
url(" http://www.myallsearch.com/{}".format(username))
url(" https://www.search.com/{}".format(username))
url(" http://www.webcrawler.com/{}".format(username))
url(" https://github.com/dchrastil/ScrapedIn/{}".format(username))
url(" http://socilab.com/{}".format(username))
url(" https://www.draugiem.lv/{}".format(username))
url(" https://www.linkedin.com/{}".format(username))
url(" http://www.pinterest.com/{}".format(username))
url(" https://www.reddit.com/{}".format(username))
url(" https://www.snapchat.com/{}".format(username))
url(" https://www.gotinder.com/{}".format(username))
url("https://www.tumblr.com/{}".format(username))
url(" https://twitter.com/{}".format(username))
url(" https://vk.com/{}".format(username))
url(" http://weibo.com/{}".format(username))
url(" https://www.xing.com/{}".format(username))
url(" https://www.youtube.com/{}".format(username))
url(" http://imgur.com{}".format(username))
url(" http://metareddit.com/{}".format(username))            
#          
#
#username = input("Username Giriniz: ")
#url("https://www.instagram.com/{}".format(username))
#url(" http://www.facebook.com/{}".format(username))
#
            
#