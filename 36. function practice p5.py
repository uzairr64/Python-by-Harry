#Define a function which counts vowels and consonant in a word.

def function(a):
    con = 0
    vowel = 0
    
    for i in range(len(a)):
        if a[i] in ["a","e","i","o","u"]:
            vowel = vowel+1
        
        else:
            con = con + 1
            
    print("Number of Vowels are" , vowel)  
    print("Number of Consonants are" , con)  
    
word = input("word:")
function(word)