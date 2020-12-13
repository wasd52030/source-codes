member_data=[]
mline_counter=0
with open('member.txt','r',encoding='UTF-8') as member:
    for line in member:
        for k in line.split():
            if mline_counter>=1:
                member_data.append(k)
        mline_counter+=1

member_data_calc=[]
for i in range(0,len(member_data),4):
    member_data_calc.append(member_data[i:i+4])


book_data=[]
book_counter=0
with open('books.txt','r',encoding='UTF-8') as book:
    for line in book:
        for k in line.split():
            if book_counter>=1:
                book_data.append(k)
        book_counter+=1

book_data_calc=[]
for i in range(0,len(book_data),3):
    book_data_calc.append(book_data[i:i+3])


borrow_data=[]
borrow_counter=0
with open('borrow.txt','r',encoding='UTF-8') as borrow:
    for line in borrow:
        for k in line.split():
            if borrow_counter>=1:
                borrow_data.append(k)
        borrow_counter+=1

borrow_data_calc=[]
for i in range(0,len(borrow_data),2):
    borrow_data_calc.append(borrow_data[i:i+2])

borrow_data_calc=sorted(borrow_data_calc,key=(lambda s:s[0]))

borrow_mids=[]
for i in range(len(borrow_data_calc)):
    borrow_mids.append(borrow_data_calc[i][0])

mids=[]
for j in range(len(member_data_calc)):
    mids.append(member_data_calc[j][0])


people_borrow=[]
people_counter=0

for i in mids:
    people_counter=0
    for j in borrow_mids:
        if i==j:
            people_counter+=1
    people_borrow.append(people_counter)


for k in range(len(member_data_calc)):
    member_data_calc[k].append(people_borrow[k])

member_data_calc=sorted(member_data_calc,key=(lambda s:s[4]),reverse=True)

class Book:
    def __init__(self,bid,btitle,publisher):
        self.bid=bid
        self.btitle=btitle
        self.publisher=publisher

book_class=[]
for i in range(len(book_data_calc)):
    b1=Book(book_data_calc[i][0],book_data_calc[i][1],book_data_calc[i][2])
    book_class.append(b1)

class Member:
    def __init__(self,mid,name,email,address,TotalBooks):
        self.mid=mid
        self.name=name
        self.email=email
        self.address=address
        self.TotalBooks=TotalBooks

member_class=[]
for i in range(len(member_data_calc)):
    m1=Member(member_data_calc[i][0],
              member_data_calc[i][1],
              member_data_calc[i][2],
              member_data_calc[i][3],
              member_data_calc[i][4])
    member_class.append(m1)

print()
print("name btitle email address publisher Total-Leading-amount")
for i in range(len(member_class)):
    for j in range(len(borrow_data_calc)):
        if borrow_data_calc[j][0]== member_class[i].mid:
            print("%-3s"%member_class[i].name,end="")
            for k in range(len(book_class)):
                if borrow_data_calc[j][1] == book_class[k].bid:
                    print("%-7s"%book_class[k].btitle,end="")
            print("%-6s"%member_class[i].email,end="")
            print("%-8s"%member_class[i].address,end="")
            for k in range(len(book_class)):
                if borrow_data_calc[j][1] == book_class[k].bid:
                    print(book_class[k].publisher,end="")
            print("%9d"%member_class[i].TotalBooks)