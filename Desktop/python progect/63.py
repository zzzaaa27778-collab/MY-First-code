word= 'wwwwooooorrrllllldddd'
def clean_world(word) :
    if len(word)<=1 :
        return word
    if   word[0] == word[1] :
            return clean_world(word[1:])
    else :
            return word[0] +  clean_world(word[1:])
clean_world(word)  
print(clean_world(word))
