# -*- coding:utf-8 -*-

# 081 if else 문
filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']
result = [x for x in filenames if x.endswith('h') or x.endswith('c') == True]
print result

# 082 큰 수 찾기
num1=10
num2=20
print max(num1, num2)

# 083 홀수 짝수 출력하기
num=10
if num % 2 == 0:
	print "Even number"
else:
	print "Odd number"

# 084 큰수 찾기
num1=10
num2=9
num3=20
print max(num1, num2, num3)

# 086 커피 가격
mydict = {'Americano':2500, 'Cafe Latte':3000, 'Cappuccino':3500}
inputorder = 'Americano'

for key, value in mydict.items():
	if key == inputorder:
		print value

# 091 역방향 순환
nums = [1, 2, 3, 4, 5]
nums.reverse()
for n in nums:
	print n

# 093 남자, 여자 구분하기
# 094 주민등록번호를 이용한 출생지 알아보기
#jumin = raw_input("주민번호 : ")
jumin = '890109-1560614'
if jumin.split('-')[1][0] == '1':
	print "Man"
else:
	print "Woman"

if jumin.split('-')[1][1:3] >= '56'\
	and jumin.split('-')[1][1:3] <= '64':
	print "전라남도"
elif jumin.split('-')[1][1:3] >= '00'\
	and jumin.split('-')[1][1:3] <= '08':
	print "서울"

# 095 주민등록번호 유효성 검사기
val=0
tmp = jumin.replace('-','')

j=2
print tmp
for i in tmp[0:len(tmp)-1]:
	val += int(i) * j
	if j >= 9 :
		j=2
	else:
		j=j+1

if 11-(val%11) == int(jumin[-1]):
	print "OK"
else:
	print "Not OK"
	
# 096 애완 동물 출력하기
pet = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']
for i in pet:
	print i, len(i)

# 100 문자열 뒤집기
mystr="python world"
result=""
for i in range(0, len(mystr)):
	result = str(mystr[i]) + result
print result

# 104 우유 배달 프로그램
milk_order = {'101': {'서울유유(200ml)':1, '남양 요구르트': 5},
              '102': {'서울우유(500ml)':2},
              '103': {'남양우유(1L)': 1, '남양 요구르트': 10},
              '104': {'서울 요구르트': 15}}

for key, value in milk_order.items():
	print key + "동"
	for k, v in value.items():
		print "%s %s개" %(k, v)


# 112 새로운 리스트 만들기
flist = ['hello.py', 'ex01.py', 'ex02.py', 'ch02.py', 'intro.hwp']
new_flist = []
for f in flist:
	if str(f).rpartition(".")[-1]:
		new_flist.append(str(f).rpartition(".")[0])
	else:
		continue
print new_flist

# 115 리스트 수정
num_list = [0, 7, 1, 2, -1, 3, -4, -5]

print(num_list)
for n in num_list:
	if n < 0:
		num_list.remove(n)
print num_list

# 120 이름이 가장 짧은 도시 출력하기
city = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']
city.sort(key=len)
result = [x for x in city if len(x)==len(city[0])]
print result
