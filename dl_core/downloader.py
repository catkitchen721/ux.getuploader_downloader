from bs4 import BeautifulSoup
import requests as rq
import os
import time
from dl_core.output_buffer import *
# https://dl1.getuploader.com/g/token/websitename/num/filename.zip
# https://ux.getuploader.com/websitename/download/num

def out2buffer(s, isCLI=False):
    print(s)
    if not isCLI:
        if len(outputBuf.get()) > 2048:
            outputBuf.set('')
        outputBuf.set(s + '\n' + outputBuf.get())
        mainW.update()

def dl_submit(website_name, min_num, max_num, passwd='', isCLI=False, exc_list=None):
    out2buffer('request submitted.', isCLI)

    dl_folder = '.\\downloads\\'
    
    if min_num > max_num:
        out2buffer('\'from\' must <= \'to\'', isCLI)
        return

    for i in range(min_num, max_num+1):
        main_url = 'https://ux.getuploader.com/'+ website_name +'/download/' + str(i)
        try:
            payload_age = {'q':'age_confirmation'}
            hd = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
            payload_psw = {'password':passwd}
            ses = rq.session()
            ses.post(main_url, headers=hd, data=payload_age)
            r = ses.post(main_url, headers=hd, data=payload_psw)
            if r.status_code == rq.codes['ok']:
                '''
                out2buffer('loaded OK: ' + main_url)
                '''
            else:
                out2buffer('Failed   : ' + main_url, isCLI)
                out2buffer('----', isCLI)
                continue
        except:
            out2buffer('Failed   : ' + main_url, isCLI)
            out2buffer('----', isCLI)
            continue
        htmltext = r.text
        soup = BeautifulSoup(htmltext, 'html.parser')
        filename = soup.find('p', attrs={'class':'space'}).find('strong').string
        if os.path.isfile(dl_folder + website_name + '\\' + filename):
            filename = str(time.time()) + '_' + filename
        out2buffer('File name: ' + filename, isCLI)
        token = soup.find('div', attrs={'class':'text-center'})
        token = token.find('input', attrs={'name':'token'})
        if token == None:
            out2buffer('Error: Maybe need password!', isCLI)
            out2buffer('----', isCLI)
            continue
        token = token['value']
        #out2buffer(token)

        dl_url = 'https://dl1.getuploader.com/g/' + token + '/' + website_name + '/' + str(i) + '/' + filename
        dl_url_chk = 'https://download1.getuploader.com/g/' + token + '/' + website_name + '/' + str(i) + '/' + filename
        used_url = dl_url
        try:
            r = rq.get(dl_url, stream=True)
            if r.status_code == rq.codes['ok']:
                r_header = dict(r.headers)
                if r_header.__contains__('Transfer-Encoding'):
                    '''
                    out2buffer('loaded OK: ' + dl_url_chk)
                    '''
                    r = rq.get(dl_url_chk, stream=True)
                    used_url = dl_url_chk
                    file_size = int(r.headers['Content-Length'])
                else:
                    '''
                    out2buffer('loaded OK: ' + dl_url)
                    '''
                    file_size = int(r.headers['Content-Length'])

                if file_size < 1024 * 1024:
                    out2buffer('File size: {:.2f}'.format(file_size/1024) + ' kb', isCLI)
                elif file_size < 1024 * 1024 * 1024:
                    out2buffer('File size: {:.2f}'.format(file_size/(1024*1024)) + ' mb', isCLI)
                else:
                    out2buffer('File size: {:.2f}'.format(file_size/(1024*1024*1024)) + ' gb', isCLI)
            else:
                out2buffer('Failed   : ' + used_url, isCLI)
                out2buffer('----', isCLI)
                continue
        except rq.RequestException:
            out2buffer('Failed   : ' + used_url, isCLI)
            out2buffer('----', isCLI)
            continue
        
        if not os.path.exists(dl_folder):
            os.mkdir(dl_folder)

        if not os.path.exists(dl_folder + website_name):
            os.mkdir(dl_folder + website_name)

        with open(dl_folder + website_name + '\\' + filename, "wb") as f:
            for chk in r.iter_content(chunk_size=32*1024):
                if chk:
                    f.write(chk)
                    f.flush()

        out2buffer('\'' + filename + '\' finished.', isCLI)
        out2buffer('----', isCLI)
        
        
