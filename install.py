import os
import requests, zipfile, io
import urllib.request
import subprocess
from bs4 import BeautifulSoup
import bs4

def update_package():
    package_list = [
        'selenium',
        'bs4',
        'twilio',
        'wappdriver',
        'pyrebase',
        'python-firebase'
    ]


    for k in package_list:
        os.system("pip3 install " + k)



def update_chromedriver():
    chromeVersion = subprocess.check_output(['/usr/bin/google-chrome', '--version']).decode('utf8')
    chromeVersion = chromeVersion.replace('Google Chrome ', '')
    chromeVersion = chromeVersion[:2]

    fp = urllib.request.urlopen("https://chromedriver.chromium.org/downloads")
    mybytes = fp.read()
    fp.close()

    ele = mybytes.decode("utf8")
    src = bs4.BeautifulSoup(ele, 'lxml')

    k = src.select('a')


    arr = []
    for j in k:
        st = j.get_attribute_list('href')
        
        if st == None or st[0] == None:
            st = ['']

        st = st[0]
        
        if st.__contains__('https://chromedriver.storage.googleapis.com/index.html?path=' + chromeVersion):
            arr.append(st)

    arr = list(set(arr))

    st = arr[0]
    chromedriver_url = st.replace("index.html?path=","")+ 'chromedriver_linux64.zip'

    dir_path = os.path.dirname(os.path.realpath(__file__))

    chromedriver = dir_path + "/chromedriver"

    if os.path.isfile(chromedriver):
        print("Deleting old chromedriver ....")
        os.system("rm "+ chromedriver)

    print("Downloading new chromedriver ....")

    r = requests.get(chromedriver_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(dir_path)

    print("Installation is comepleted successfully!!")





# update_package()
# update_chromedriver()


