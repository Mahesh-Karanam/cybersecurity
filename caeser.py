def isValid(message):
    for i in message:
        if ord(i) not in range(65,91) and ord(i) not in range(97,123) and not i.isdigit() and i != " ":
            print("invalid message")
            return False
    return True
message=input("Enter a message: ")
key=(int(input("Enter Key: ")))%26
caeser=""
if isValid(message):
    for i in message:
        if i == " ":
            caeser+= " "
            continue
        if i.isupper():
            caeser+=chr((ord(i)-65+key)%26 + 65)
        elif i.isdigit():
            caeser+= str((int(i)+key)%10)
        else :
            caeser+=chr((ord(i)-97+key)%26 + 97)
print(caeser)


print("____BRUTE FORCING____")

def decrypt(cipher,k):
    dec=""
    for c in cipher:
        if c== " ":
            dec+=" "
            continue
        if c.isupper():
            dec+=chr((ord(c)-65-k)%26 + 65)
        elif c.isdigit():
            dec+=str((int(c)-k)%10)
        else :
            dec+=chr((ord(c)-97-k)%26 + 97)
    return dec

def brute(caeser):
    for k in range(1,27):
        if decrypt(caeser,k) == message:
            print(message,"\t",k)
            break
        else :
            print(decrypt(caeser,k),"\t",k)
brute(caeser)
        
        
        

