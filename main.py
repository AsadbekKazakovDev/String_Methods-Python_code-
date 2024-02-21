#String methods of examples

#Method name ->capitalize()

# a = "Hello Samarkand"
# ans = a.capitalize()
# print(ans)#Hello samarkand

#Method name ->casefold()

# a = "Hello Samarkand"
# ans = a.casefold()
# print(ans)

#Method name ->center()

# a = "Asadbek Kazakov"
# b = a.center(50,"1")
# print(b)#11111111111111111Asadbek Kazakov111111111111111111

#Method name ->count()

# a = "Asadbek Kazakov"
# cnt = a.count("a")
# print(cnt)#3

#Method name ->encode()

# a = "Samarkand"
# b = a.encode()
# print(b)#b'Samarkand'

#Method name ->endswith()

# a = "Hello Samarkand"
# b = a.endswith("and")
# print(b)#True

#Method name ->expandtabs()

# a = "Hello\tSamarkand"
# b = a.expandtabs(10)
# print(a)#Hello   Samarkand
# print(b)#Hello     Samarkand

#Method name ->find()

# a = "Asadbek Kazakov"
# b = a.find("b")
# c = a.find(" ",0,10)
# print(b)#4
# print(c)#7

#Method name ->format()

# a = "Men {group_name} guruh talabasi {my_name} {my_surename}man".format(group_name="DI 20-11",my_name="Asadbek",my_surename="Kazakov")
# print(a)#Men DI 20-11 guruh talabasi Asadbek Kazakovman

#Method name ->format_map()

# a = {'group_name':'DI 20-11','my_name':'Asadbek','my_surename':'Kazakov'}
# b = 'Men {group_name} guruh talabasi {my_name} {my_surename}man.'
# ans = b.format_map(a)
# print(ans)#Men DI 20-11 guruh talabasi Asadbek Kazakovman.

#Method name ->index()

# a = "Asadbek Kazakov"
# b = a.index("Kazakov")
# print(b)#8

#Method name -> isalnum()

# a= "Asadbek Kazakov"
# b= a.isalnum()
# print(b)#False

#Method name ->isalpha()

# a = "Asadbek Kazakov"
# b = a.isalpha()
# print(b)#False

#Method name ->isascii()

# a = "28- IDUMI"
# b = a.isascii()
# print(b)#True

#Method name ->isdecimal()

# a = "12345"
# b = a.isdecimal()
# print(b)#True

#Method name ->isdigit()
#
# a = "1290"
# b = a.isdigit()
# print(b)#True

#Methods name -> isidentifier()

# a = "IDuMI009"
# b = a.isidentifier()
# print(b)#True

#Methods name -> islower()

# a = "samarkand"
# b = a.islower()
# print(b)#True

#Methods name -> isnumeric()

# a = "2024"
# b = a.isnumeric()
# print(b)#True

#Methods name -> isprintable()

# a = "2024yil\n2023"
# b = a.isprintable()
# print(b)#False
#
# a = "2024yil2023"
# b = a.isprintable()
# print(b)#True

#Methods name ->isspace()

# a = "  A"
# b = a.isspace()
# print(b)#False
#
# a = "  "
# b = a.isspace()
# print(b)#True

#Method name ->istitle()

# a = "Men Samarqand Viloyatida Yashayman"
# b =a.istitle()
# print(b)#True
#
# a = "Men Samarqand Viloyatida yashayman"
# b =a.istitle()
# print(b)#False

#Method name ->isupper()

# a = "SAMARQAND"
# b = a.isupper()
# print(b)#True
#
# a = "sAMARQAND"
# b = a.isupper()
# print(b)#False

#Method name ->join()

# a = "Men Asadbek Kazakovman"
# tst = "#"
# b = tst.join(a)
# print(b)#M#e#n# #A#s#a#d#b#e#k# #K#a#z#a#k#o#v#m#a#n

#Method name ->ljust()

# a = "Samarkand"
# b = a.ljust(20)
# print(b,"Live")#Samarkand            Live
#
# a = "  Samarkand"
# b = a.ljust(20,"0")
# print(a+"Live")#  SamarkandLive

#Method name ->lower()

# a = "Asadbek Kazakov"
# b = a.lower()
# print(b)#asadbek kazakov

#Method name ->lstrip()

# a = "     Asadbek     "
# b  = a.lstrip()
# print("Men "+b+"Kazakovman")#Men Asadbek     Kazakovman

#Method name ->maketrans()

# a = "Learn"
# b = str.maketrans("Learning","pythonGO")
# print(a.translate(b))#pythG

#Method name ->partition()

# a = "Hello, Samarkand"
# b = a.partition(",")
# print(b)#('Hello', ',', ' Samarkand')

#Method name ->replace()

# a = "Learn Python"
# b = a.replace("Python","C++")
# print(b)#Learn C++

#Method name->rfind()

# a = "Hello Samarkand"
# b=a.rfind("Sam")
# print(b)#6

#Method name ->rindex()

# a = "Learn Python"
# b = a.rindex("t")
# print(b)#8

#Method name-> rjust()

# a="Hello Samarkand"
# b=a.rjust(20)
# print(b)#     Hello Samarkand

#Method name->rpartition()

# a = "Learn By example Python"
# b=a.rpartition(",")
# print(b)#('', '', 'Learn By example Python')

#Method name->rstrip()
#
# a = "Hello World"
# b=a.rstrip('Wldor')
# print(b)#Hello

#Method name->rsplit()

# a = "Hello Samarkand"
# b = a.split(" ")
# print(b)#['Hello', 'Samarkand']

#Method name->split()

# a = "Hello Samarkand ahli"
# b=a.split(" ")
# print(b)#['Hello', 'Samarkand', 'ahli']

#Method name-> splitlines()

# a = "Hello\nSamarkand"
# b = a.splitlines()
# print(b)#['Hello', 'Samarkand']

#Methods name-> startswith()

# a = "Hello Samarkand"
# b = a.startswith("Hello")
# print(b)#True

#Methods name-> strip()

# a = "hello samarkand"
# b = a.strip("olehol")
# print(b)#Samarkand

#Methods name->swapcase()

# a = "Hello Samarkand"
#
# b = a.swapcase()
# print(b)#hELLO sAMARKAND

#Methods name ->title()

# a = "Python vs C++"
# b=a.title()
# print(b)#Python Vs C++

#Methods name ->translate()

# a = "Hello Golang"
# b=str.maketrans("Golang","Python")
# print(a.translate(b))#Hetty Python

#Methods name -> upper()

# a = "hello world"
# b=a.upper()
# print(b)#HELLO WORLD

#Methods name-> zfill()

# a = "Hello"
# b = a.zfill(10)
# print(b)#00000Hello

