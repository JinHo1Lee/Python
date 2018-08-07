# -*- coding:utf-8 -*-

# 041 리스트 생성
mylist=[[1, "닥터스트레인지"], [2, "스플릿"], [3, "럭키"]]
mystr='한글'
print repr(mylist).decode('string-escape')

# 043 리스트 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print langs

# 044 최댓값, 최솟값
nums = [1, 2, 3, 4, 5, 6, 7]
print "최소값 : %d" %min(nums)
print "최대값 : %d" %max(nums)

# 046 리스트 reverse
tlist = ['2016-09-05', '2016-09-06', '2016-09-07', '2016-09-08', '2016-09-09']
tlist.sort(reverse=True)
print tlist

# 047 평균값 계산
close_price_daeshin = [10000, 10500, 10300, 10700, 11100]
print float(sum(close_price_daeshin) / len(close_price_daeshin))

# 048 리스트 형 변환
data = ['a', 'b', 'c', 'd', 'e']
print type(tuple(data))

# 049 리스트 삭제 # 050 join
nums = [1, 2, 3, 4, 5]
nums.pop()
nums.pop()
print nums

nums.append(4)
print nums

# 050 join
items = ['000600', '034560', '003540', '039490']
print ";".join(items)

# 052 리스트 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
mylist = list(interest)
print repr(interest).decode('string-escape')
print repr(mylist).decode('string-escape')

# 053 튜플 만들기
t = (1, 2, 3, 4, 5)
print t[1]
print t[3]

t = ('a', 'b', 'c')
mylist = list(t)
mylist[0] = mylist[0].upper()
t = tuple(mylist)
print t

# 062 딕셔너리에 값 추가
mydict={}
print type(mydict)
mydict['Melona']  = 1000
mydict['Pollapo'] = 1200
mydict['Ppangppare'] = 1800
mydict['Tankboy'] = 1200
mydict['Heathunting'] = 1200
mydict['Worldcom'] = 1500
print mydict['Melona']
mydict['Melona'] = 1300
print mydict['Melona']
mydict['Melona'] = 1000

# 065 딕셔너리와 리스트
mydict = {'Melona':[1000, 10], 'Pollapo':[1200,7], 'Ppangppare':[1800, 6], 'Tankboy':[1200, 5], 'Heathunting':[1200,4], 'Worldcorn':[1500,3]}
print mydict

# 067 딕셔너리 keys
# 068 딕셔너리 values
icecream = {'Tankboy': 1200, 'Pollapo': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000, 'Heathunting': 1200}
mylist = list(icecream.keys())
print mylist
mylist = list(icecream.values())
print mylist

# 069 딕셔너리 update
contact1 = {'chusu': '010-3111-2393', 'minsu':'010-3112-9932'}
contact2 = {'jaein': '011-1312-2121', 'jongho':'010-8821-1311'}
contact = {}
contact.update(contact1)
contact.update(contact2)
print contact

# 071 List comprehension
nums = [1, 2, 3, 4, 5]
nums = [1*x*x for x in nums]
print nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in nums if x%2==0]
odd = [x for x in nums if x%2!=0]
print even
print odd

files = ['a.txt', 'b.txt', 'exer.avi', 'sing.mp3', 'ultra.avi']
files = [x for x in files if x[-4:] == ".txt"]
print files

# 075 Star expression
def sum(a, b) :
    return a + b

var = [10, 11]
print sum(*var)

# 076 List sorting과 slicing
nums = [-1, 10, 2, 8, 9, 7, -11, 20, 21, 37, 56, 21, -27]
nums.sort()
print nums[-3:len(nums)]
print nums[0:3]

# 077 Set 자료구조 중복값 없애기
items = [1, 6, 2, 3, 4, 4, 6, 6, 7, 2, 7]
new_items = list(set(items))
print new_items

# 078 두개의 리스트로부터 딕셔너리 생성
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
end_price = [10500, 10300, 10100, 10800, 11000]
deashin = dict(zip(date, end_price))
print deashin

# 079 정렬
strs = ['for', 'example' 'with', 'a', 'list']
newstrs = sorted(strs, key=len)
print newstrs

# 080 리스트와 range
nums = list(range(10))
print nums
