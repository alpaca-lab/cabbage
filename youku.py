import webbrowser
import time


def youku(fp,num):
    counter=0
    while(counter < num):
        webbrowser.open(fp)
        counter += counter
        time.sleep(30)


if __name__=="__main__":
    path="http://v.youku.com/v_show/id_XMzE1NTY3Njk0NA==.html?spm=a2h0j.8191423.playlist_content.5!9~5~5~A&&f=51249681&from=y1.2-3.4.9"
    youku(path,20)
