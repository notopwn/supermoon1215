from bs4 import BeautifulSoup

# import urllib3
# import urllib
# from pip._vendor.distlib.compat import raw_input
#
#
# def getdictionarysearch(w):
#     response=urllib.request.urlopen("https://terms.naver.com/search.nhn?query="+w)
#     soup=BeautifulSoup(response)
#
#     result=""
#     result+=soup.find('dd',{'class':'dsc'}).get_text().encode('UTF-8')
#
#     a = soup.find('ul',{'class':'thmb_lst',}).find('li').find('dt').find('a')
#
#     result += "\n[url]\n"+"https://terms.naver.com"+a["href"].encode('utf-8')
#
#     return result
#
# w = raw_input('enter word something')
# print (getdictionarysearch(w))

import sys
import requests
from bs4 import BeautifulSoup
def search_daum_dic(query_keyword):
    dic_url = """http://dic.daum.net/search.do?q={0}"""
    r = requests.get(dic_url.format(query_keyword))
    soup = BeautifulSoup(r.text, "html.parser")
    result_means = soup.find_all(attrs={'class':'list_search'})
    print_result("daum", result_means)
def print_result(site, result_means):
    print("*" * 25)
    print("*** %s dic ***" % site)
    print("*" * 25)
    for elem in result_means:
        text = elem.get_text().strip()
        if text:
            print(text.replace('\n', ', '))
        print()
def main(args=None):
    """The main routine."""
    if len(sys.argv) < 2:
        print("Usage : daumdic [keyword]")
        sys.exit(0)
    query = sys.argv[1]
    try:
        search_daum_dic(query)
    except:
        print("Please check your internet connection.")
if __name__ == "__main__":
    main()

