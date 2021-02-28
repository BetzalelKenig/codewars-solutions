# Among the ruins of an ancient city a group of archaeologists found a mysterious function with lots of HOLES in it called getNum(n) (or get_num(n) in ruby, python, or r). They tried to call it with some arguments. And finally they got this journal:

# getNum(300) #-> returns 2
# getNum(90783) #-> returns 4
# getNum(123321) #-> returns 0
# getNum(89282350306) #-> returns 8
# getNum(3479283469) #-> returns 5

# The archaeologists were totally stuck with this challenge. They were all in desperation but then.... came YOU the SUPER-AWESOME programmer. Will you be able to understand the mystery of this function and rewrite it?

def get_num(n):
    count = 0
    for i in str(n):
        if i in '069':
            count += 1
        if i == '8':
            count += 2
    return count
