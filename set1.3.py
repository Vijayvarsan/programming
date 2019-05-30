ch=input("enter a character:")
vowels=['a','e','i','o','u']
consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if ch in vowels:
    print("vowel")
elif ch in consonant:
    print("consonant")
else:
    print("invalid")
    
