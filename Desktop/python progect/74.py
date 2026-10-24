from functools import reduce
figures=[10,20,30,26,66,123]
def my_text(text1,text2) :
    return text1 * text2 
back= reduce(my_text,figures)
print(back)
back = reduce(lambda text1 ,text2 : text1*text2,figures)
print(back)
figures. remove(123)
print(figures)
    