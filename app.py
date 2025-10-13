import requests, re

def header(url):
    print("[+] -> URL:", url);
    r = requests.get( url )
    # accessing response headers 
    return r.headers

def remove(h):
    lista = [];
    allow = open("allow.txt", "r").readlines();
    deny  = open("deny.txt",  "r").readlines();
    for key in h.keys():
        encontrado = False;
        valor = (key.strip() + ":" + h[key].strip()).lower();
        for i in range(len(allow)):
            comp = re.compile( allow[i].strip().lower() );
            if comp.match( valor ):
                encontrado = True;
                break;
        if encontrado:
            print("\t", "\033[92m", key, "\t\t", h[key], "\033[0m");
            continue;
        for i in range(len(deny)):
            comp = re.compile( deny[i].strip().lower() );
            if comp.match( valor ):
                encontrado = True;
                break;
        if encontrado:
            print("\t", "\033[91m", key, "\t\t", h[key], "\033[0m");
            continue;
        print("\t", "\033[93m", key, "\t\t", h[key], "\033[0m");

links = open("urls.txt", "r").readlines();
for link in links:
    h = header(link.strip())
    remove(h);