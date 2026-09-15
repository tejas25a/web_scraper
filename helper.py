# 1 layer scrape
from bs4 import BeautifulSoup as bs
import requests as rq
import sys, getopt

def parse_func(hf):
    try:
        soup = bs(hf,"html.parser")
        links = [a.get("href") for a in soup.find_all("a")]
        links_type = [a.get("class") for a in soup.find_all("a")]
        links_dict = dict(zip(links, links_type))
        return links_dict

    except:
        print("Error in parse_func")

def req(link):
    try:
        link = sys.argv[2] 
        response = rq.get(link)
        if 200 == response.status_code:
            hf = response.content
            return hf

    except:
        print("Error in req")

def usage():
    print("""Usage:
python helper.py -l <link>
    """)

def helper_main():
    args = sys.argv[1:]
    options = "l"
    try:
        arguments, values = getopt.getopt(args, options)
        if (len(sys.argv) != 3):
            usage()
            return
        for currentArg, currentVal in arguments:
            if currentArg in ("-l"):
                link = sys.argv[2]
                hf = req(link)
                lds = parse_func(hf)
                links_str = str(lds).replace(",","\n")
                with open("result_links.txt","w") as f:
                    f.write("========"+link+"========\n")
                    f.write("links:\n")
                    f.write(links_str)
                    f.write("\n\n")


    except getopt.error as err:
        print(str(err))
helper_main()
