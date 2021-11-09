
# Hello sir, this is Christopher Drape! This is my first time coding with Python
# and for some reason I always have missing characters or an output that's different 
# from your sample data. I think this is because of my coding environment.

# It would be appreciated if you could give me a little feedback on what I have 
# done wrong here because I am pretty clueless right now Hahaha. If you're
# busy that's fine too! Thank you for your time sir!

p=11
q=13

n = p*q
z=(p-1)*(q-1)
e= 7
d =223

phrase1 = "ENCRYPTION"
dphrase1 = "lNYECaHS(N"

phrase2 = "RASTAMAN"
dphrase2 = "EA█HAMAN"  #Replace the 'backspace' with a box?


def encrypt(p, q, phrase):
    
    encryptPhrase=""
    
    for x in phrase:  #loop through word
       # print(x)
        m =pow(ord(x),e,n) #Power Of and Modulo
       # print (m)
        encryptPhrase =encryptPhrase +chr(m)
    
    print("The Newly Encrypted Phrase: "+encryptPhrase)
    
def decrypt(p,q,phrase):
    decryptPhrase=""
    for x in phrase: #loop through word
       # print(x)
        c=pow(ord(x),d,n) #Power of and Modulo
       # print (c)
        decryptPhrase = decryptPhrase +chr(c)
    print("The Newly Decrypted Phrase: "+decryptPhrase)

encrypt(p,q,phrase1)
decrypt(p,q,dphrase1)

encrypt(p,q,phrase2)
decrypt(p,q,dphrase2)



