#This program opens a file and check its content to see if it has
#bad language in it and displays a message with the result

import urllib.request

def check_file():
    content = open("C:/Python/tmp/some_file.txt")
    file_content = content.read()
    #print(file_content)
    content.close()
    check_profanity(file_content)

def check_profanity(text_to_check):
    text_to_check = urllib.request.quote(text_to_check)
    with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) as url:
        s = url.read()
        if (str(s) == "b'true'"):
            print("Bad language")
        else:
            print("No bad language")
        #print(s)
        #s.close()  // not necessary "with" closes it automatically
    

check_file()
