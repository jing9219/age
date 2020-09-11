driving = input('請問你有沒有開過車？ ')
if driving != 'yes' and driving != 'no':
	print('只能回答 yes/no')
	raise SystemExit

age = input('請輸入年齡： ')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('恭喜符合資格')
	else:
		print('奇怪 你怎麼能開車？')
elif driving == 'no':
	if age >= 18:
		print('怎麼不去考駕照？')
	else:
		print('沒關係 再過幾年就可以開車了')
