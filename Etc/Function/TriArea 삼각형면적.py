def area_tri(a,b):
    c = a * b /2
    print('순서2')
    area_print(c)
    print('순서4')

def area_print(c):
    print('순서3')
    print('삼각형의 면적은',c)

print('순서1')
a = int(input("가로의 길이"))
b = int(input("세로의 길이"))

area_tri(a,b)
print('순서5')
