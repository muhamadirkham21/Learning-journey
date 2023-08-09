
# create simple web browser
# with socket
import socket 
import urllib.request, urllib.parse, urllib.error

def with_socket():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if len(data) < 1 :
            break
        print(data.decode())

    mysocket.close()

def with_urlib():
    fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
    for line in fhand:
        print(line.decode().strip()) # berlaku untuk txt, html


# contoh implementasi
def count_word(url):
    count={}
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        words = line.decode().split()
        for word in words:
            count[word] = count.get(word, 0) + 1
    print(count)

count_word('http://data.pr4e.org/romeo.txt')