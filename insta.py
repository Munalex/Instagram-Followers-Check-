from instagrapi import Client
import argparse

parser = argparse.ArgumentParser(description="Script for interacting with Instagram")
parser.add_argument('-user', required=True, help='Instagram User')
parser.add_argument('-password', required=True, help='Instagram Password')

args = parser.parse_args()


usuario = args.user
contra = args.password


cl = Client()
cl.login(usuario, contra)

seguidores_lista = [] 
seguidos_lista = []


seguidos = cl.user_following(cl.user_id)
seguidores = cl.user_followers(cl.user_id)

for user_id, user_info in seguidores.items():
    username = user_info.username
    seguidores_lista.append(username)



for user_id, user_info in seguidos.items():
    username = user_info.username
    seguidos_lista.append(username)

archivo = open("seguidores.txt","w")
for bucle in seguidos_lista:
    if bucle not in seguidores_lista:
        archivo.write(bucle + 1 * ' ' + "nope" + "\n")



print("Done!")
