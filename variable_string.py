# -*- coding:utf-8 -*-

# 1
print "Hello World"

# 2
print "Mary's cosmetics"

# 3
print "{0:.2f}".format(3.141592)

# 4
a=input("first : ")
b=input("second : ")
print "합 : %d" %(a+b)

# 5
s=raw_input("문자열: ")
n=input("반복횟수 : ")
print s*n

# 6
s="720"
n=int(s)
print "%d" %n
n=100
s=str(n)
print "%s" %s

# 7
print("first", end='')
print("second")

# 8
a=1
print type(a)

# 021 문자열 합치기
companies=['NAVER', 'KAKAO', 'SK', 'SAMSUNG']
print ";".join(companies)

# 022 문자열 나누기
companies = '000660;060310;0133340;095570;068400;006840'
print companies.split(';')

# 023 문자열 잘라내기
code = '         000660\n            '
print code.strip()

# 024 문자열의 마지막 패턴 매칭
filename = "run.py"
if filename[-3:len(filename)] == ".py":
	print "python file"
else:
	print "unknown extension"

# 025 문자열 인덱싱
# 026 문자열 변경
letters="python"
print letters[0]
print letters[2]
print letters.replace('p', 'P')

# 029 도메인 추출
address = "http://www.wikidocs.net/edit/page/7022"

for tmp in address.split('/'):
	if tmp[0:3] == "www":
		t = tmp[-4:len(tmp)]
		if t == ".com" or t ==".net" or t == ".org":
			print "address : %s" %(address)
			print "domain : %s" %(t)

# 032 count 메서드
introduce = "python is widely used high-level language. python was conceived in the late 1980s"
print introduce.split().count('python')

# 034 zfill 메서드
mystr = "13"
print mystr.zfill(5)

# 035 strip 메서드
mystr = "a man goes into the room..."
print mystr.strip('...')

# 037 경로분리
mystr = "c:\\program files\\python"
print mystr.split('\\')[-1]

# 038 문자열 분리 및 합치기
mystr = "spam egg"
mylist = mystr.split(' ')
mylist.reverse()
print ", ".join(mylist)

# 039 문자열 개수 확인
mystr = 'Python python pYthon java Java'
print mystr.lower().count('python')

mystr = "10:00:01"
mylist = mystr.split(":")
print int(mylist[0])*3600 + int(mylist[1])*60 + int(mylist[2])
