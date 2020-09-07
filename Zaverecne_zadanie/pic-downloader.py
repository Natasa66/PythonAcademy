#
# pip install requests
#
#importy

#
import requests
import requests.exceptions
import re
import os

import argparse

#---------------------------------------------------------------------------------------
# get argument - webpage
"""
def get_argument():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()

    url_l = args.file
    return url_l
    """
#--------------------------------------------------------------------------------------
def je_to_webova_stranka(url):
    try:
        r = requests.head(url)
        return r.status_code == 200
    except:
        return False


def get_url():
    url_l = ""
    stranka_je_OK = 0
    pocet_pokusov = 0
    while(stranka_je_OK == 0 and pocet_pokusov < 10):
        pocet_pokusov += 1
        url_l = str(input("Zadaj webovu stranku (celu adresu): "))
        #            url_l = "https://" + url_l
        stranka_je_OK = je_to_webova_stranka(url_l)

    return url_l

#---------------------------------------------
#get the list of pictures
#---------------------------------------------
def get_all_images(url_l):
    website = requests.get(url_l)
    html = website.text
    pattern = re.compile(r'<\s*img [^>]*src="([^"]+)')
    img = pattern.findall(html)
    return img

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

if __name__ == "__main__":
#    url = get_argument()
    url = get_url()
    if len(url) == 0:
        print("koniec")
    else:
        img_list = get_all_images(url)
        pathname = input("Kam ich mam ulozit?: ")
        # if path doesn't exist, make that path dir
        if not os.path.isdir(pathname):
            os.makedirs(pathname)
        print(f"Zapisujem subory do adresara {pathname}")
        for image in img_list:
            try:
                pos = image.index("?")  # if there is "? extension" - delete it
                img_url = image[:pos]
                imagename = img_url.split('/')[-1]   # get name of image file from url adress
                filename = os.path.join(pathname, imagename)
                r = requests.get(img_url,allow_redirects=True)
                open(filename,'wb').write(r.content)
            except ValueError:
                pass
        print("Koniec")



