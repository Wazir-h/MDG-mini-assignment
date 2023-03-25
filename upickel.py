from pickle import *
import click

def search(key,f):
    f.seek(0) 
    d = {}
   
    flag = False 
    try:
        while True:
            d = load(f)
            if key in d:
                flag = True
                D=d 

    except EOFError:
        if flag:
            return D
        else:
            pass
        

def entry(d,f): 
    dump(d,f)

def desc(f): 
    f.seek(0)
    d = {} 
    try:
        while True:
            d = load(f) 
            click.echo(d)
    except EOFError: 
        pass


def update(key,up_dat,f): 

    with open(f,"rb") as file:
        l = []
        file.seek(0)
        d = {}
        try:
            while True:
                d = load(file)
                if key in d:
                    d[key] = up_dat 
                    l.append(d)
                else:
                    l.append(d)
        except EOFError: 
            pass
    
    with open(f,"wb") as file:
        for k in l:
            dump(k,file)