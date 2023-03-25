#!/usr/bin/env python
import upickel
import click

import datetime 
import json
from passgen import PasswordGenerator


d = {
    "y" : True,
    "n" : False
}


@click.command()
@click.option("--plen",prompt = "Enter password length", type = int) 
@click.option("--schar",prompt = "Enter special char you wish to include",type = str) 
@click.option("--flagn",prompt = "Do you wish to include numbers (y/n)") 
@click.option("--purpose",type = str,prompt = "Write your purpose of password") 

def gen(plen ,schar, flagn,purpose):
    
    generation_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    flagn = d[flagn]

    p = PasswordGenerator(schar,plen,flagn)
    p.generate()
    pswd = p.finalpass

    with open("pass_file.dat","ab+") as passfile:
        upickel.entry({purpose:pswd},passfile)
    click.echo(f"Your password for {purpose} has been written successfully.\n{generation_time}")
    click.echo(f"Your password is:\t {pswd}\t")

    generation_time = generation_time.split(' ')
    data = {
        "date": generation_time[0],
        "time":generation_time[1],
        "purpose":purpose,
        "sha1" : p.hashedpass()[0],
        "sha256" : p.hashedpass()[1]
    }

    with open("hashed_script.txt","a+") as hash:
        json.dump(data,hash,indent=4)

    click.echo("Hashed value is stored in file 'hashed_script.txt' ")





@click.command()
@click.option("--purpose",prompt = "Enter purpose",type = str) 
def acs(purpose):
    passfile = open("pass_file.dat","rb")
    y = upickel.search(purpose,passfile)
    passfile.close()
    if(type(y) == dict):    click.echo(f"Your pswd for {purpose} is: \t{y[purpose]}\t")
    else:   click.echo(y)


@click.command()
def desc():
    passfile = open("pass_file.dat","ab+")
    upickel.desc(passfile)
    passfile.close()





@click.command()
@click.option("--purpose",prompt = "Enter purpose",type = str) 
@click.option("--npass",prompt = "Enter New password",type = str) 

def updt(purpose,npass):
    upickel.update(purpose,npass,"pass_file.dat")
    click.echo("Your password has been updated successfully.")

    click.echo({purpose:npass})

    generation_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    generation_time = generation_time.split(' ')

    p = PasswordGenerator().hashedpass(npass)
    data = {
        "date": generation_time[0],
        "time":generation_time[1],
        "record":f"updated pswd for {purpose}",
        "sha1":p[0],
        "sha256":p[1]
    }

    with open("hashed_script.txt","a+") as hash:
        json.dump(data,hash,indent=4)






@click.group()
def command_group():
    pass

command_group.add_command(acs)
command_group.add_command(gen)
command_group.add_command(desc)
command_group.add_command(updt)




if __name__ == "__main__":

    print('''
            
    \u001b[33m░█████╗░██╗░░░░░██╗  ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
    ██╔══██╗██║░░░░░██║  ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
    ██║░░╚═╝██║░░░░░██║  ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
    ██║░░██╗██║░░░░░██║  ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
    ╚█████╔╝███████╗██║  ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
    ░╚════╝░╚══════╝╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
    ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
    ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\u001b[0m
    ''')
    command_group()
