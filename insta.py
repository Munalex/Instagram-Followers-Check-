# Import the library
from typing import OrderedDict
import instaloader


instagram = instaloader.Instaloader()


usuario = "Neo" # Instagram User
contra = "Wh1terabb1t" # Instagram Password
instagram.login(usuario,contra) #login

# Obtain the profile
profile = instaloader.Profile.from_username(instagram.context,usuario)

#list of Followers and followees
seguidores_lista = [] 
seguidos_lista = []

#get the followers
for seguidores in profile.get_followers():
    seguidores_lista.append(seguidores.username)

#get the followees 
for seguidos in profile.get_followees():
    seguidos_lista.append(seguidos.username)

#compare the followers with the followees
archivo = open("seguidores.txt","w")
for bucle in seguidos_lista:
    if bucle not in seguidores_lista:
        archivo.write(bucle + 1 * ' ' + "nope" + "\n")

