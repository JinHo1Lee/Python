# -*- coding:utf-8 -*-

# 125 2의 보수 계산하기
def twos_complement(a):
	result=""

	c=abs(a)
	i=1
	while ( c > 0):
		b = c % 2
		result = str(b) + result
		c = c / 2

	result = result.rjust(8,'0')
	if a < 0:
		result = '1' + result[1:]

	return result

print "1 : %s" %twos_complement(1)
print "20 : "+twos_complement(20)
print "-1 : %s" %twos_complement(-1)
print "-20 : %s" %twos_complement(-20)

# 132 통신사 알아내기
tel='01112345678'
teldic={'011':'SKT', '016':'KT', '019':'LGT'}
for key, value in teldic.items():
	if key == tel[0:3]:
		print value

# 136 문자열 합치기
def add_str(*argv):
	result=""
	for c in argv:
		result += c + " "
	return result

# 138 짝수 고르기
def pickup_even(items):
	new_item = []
	for i in items:
		if i % 2 == 0:
			new_item.append(i)
	return new_item

print pickup_even([1, 2, 3, 4])


# 143 로또 번호 생성기
import random

def lotto_number():
	mylotto = []
	while True:
		num = random.randint(1, 45)
		for lottonum in mylotto:
			if num == lottonum:
				continue
		mylotto.append(num)
		if len(mylotto) == 6:
			break
	return mylotto

print lotto_number()
