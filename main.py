import re
import requests as req

#Takes a url request of a given website, with optional parameters and optionally saves its content 
#to a file
#Args:
#       url (String): link to the webiste
#       params (dictionary)(optional): parameters to be passed
#       output (string): name of the file to be saved to, should end with .txt
#Returns: 
#        if an output argument is defined a text file is created
#        else the response of the webiste is just returned

def get_html(url, params=None, output=None):


        resp=req.get(url, params=params)

        tekst = str(resp.text)
        if(output != None):
                f = open(output, "w")
                f.write(tekst)
                f.close() 
       
        # If the optional output argument is not set, the response is just returned
        else:
                return resp.text

#Find all urls from a website, stores them in list and returns the list
#Args:
#       html_string (string): link to webiste
#Returns:
#       all_urls (list): A list containing all the urls found in the given website
def find_urls(html_string):
        
        # Can reuse the function from earlier exercise
        text = get_html(html_string) 

        normal_urls = r"<a href=\"((?:https|http)://\w+(?:\W\w+)+)"
        relative_urls = r"<a href=\"(//\w+(?:\W\w+)+)"
        relative_urls2 = r"<a href=\"(/\w+(?:\W\w+)+)"
        matches = re.findall(normal_urls, text)
        matches2 = re.findall(relative_urls, text)
        matches3 = re.findall(relative_urls2, text)

        new_matches3 = []
        for m in matches3:
                new_matches3.append("https://en.wikipedia.org" + m)

        all_urls = matches + matches2 + new_matches3

        return all_urls

#Find all wikipedia article urls from a website, stores them in list and returns them
#Optionally saves them to a file if output argument is specified
#Args:
#       html_string (string): link to webiste
#       output (string)(optional): name of the file to be saved as
#Returns:
#       wikipedia_url_list (list): A list containing all the wikipedia articles
#       urls from the given website
def find_articles(url, output=None):
        wikipedia_urls = re.compile("https://[a-z]+.wikipedia.+")
        url_list = find_urls(url)
        
        if(output):
                f = open(output, "w")
                f.write("Result from find_urls function\n")
                for u in url_list:
                        f.write(u + "\n")
                f.write("\n\n\n")
                f.close()

        wikipedia_url_list = list(filter(wikipedia_urls.match, url_list))

        if(output):
                f = open(output, "a")
                f.write("Result from find_articles function\n")
                for u in wikipedia_url_list:
                        f.write(u + "\n")
                f.close()

        return wikipedia_url_list

if __name__ == "__main__":
        find_articles("https://en.wikipedia.org/wiki/Nobel_Prize","test1.txt")
        find_articles("https://en.wikipedia.org/wiki/Bundesliga", "test2.txt")
