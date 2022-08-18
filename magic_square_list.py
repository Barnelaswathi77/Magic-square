a=[[8,3,4,],
   [1,5,9],
   [6,7,2]]
i=0
r1=0
r2=0
r3=0
while i<len(a):
    j=0
    while j<len(a):
        if i==0:
            r1=r1+a[i][j]
        elif i==1:
            r2=r2+a[i][j]
        else:
            r3=r3+a[i][j]    
        j=j+1
    i=i+1
if r1 ==r2==r3:
    print("row1",r1)
    print("row2",r2)
    print("row3",r3)
else:
    print("not equal",r1,r2,r3)
i=0
c1=0
c2=0
c3=0
while i<len(a):
    j=0
    while j<len(a):
        if i==0:
            c1=c1+a[i][j]
        elif i==1:
            c2=c2+a[i][j]
        else:
            c3=c3+a[i][j]
        j=j+1
    i=i+1
if c1==c2==c3:
    print("col1",c1)
    print("col2",c2)
    print("col3",c3)
else:
    print("not equal",c1,c2,c3)
i=0
d1=0
d2=0
while i<len(a):
    j=0
    while j<len(a):
        if i==0:
            d1=d1+a[i][j]
        elif i==1:
            d2=d2+a[i][j]
        j=j+1
    i=i+1
if d1==d2:
    print("daigonal",d1+d2)
    
else:
    print("not equal",d1,d2)



# a=[[8,3,4],
#    [1,5,9],
#    [6,7,2]]
# i=0
# r1=0
# r2=0
# r3=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if i==0:
#             r1=r1+a[i][j]
#         elif i==1:
#             r2=r2+a[i][j]
#         j=j+1
#     i=i+1
# if i==r1==r2==r3:
#     print("row1",r1)
#     print("row2",r2)
#     print("row3",r3)
# else:
#     print("not equal",r1,r2,r3)
# i=0
# c1=0
# c2=0
# c3=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if i==0:
#             c1=c1+a[i][j]
#         elif i==1:
#             c2=c2+a[i][j]
#         else:
#             c3=c3+a[i][j]
#         j=j+1
#     i=i+1
# if i==c1==c2==c3:
#     print("col1",c1)
#     print("col2",c2)
#     print("col3",c3)
# else:
#     print("not equal",c1,c2,c3)
# i=0
# d1=0
# d2=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if i==0:
#             d1=d1+a[i][j]
#         else:
#             d2=d2+a[i][j]
#         j=j+1
#     i=i+1
# if i==d1==d2:
#     print("dai1",d1)
#     print("dai2",d2)
# else:
#     print("not equal",d1,d2)







        




        


   