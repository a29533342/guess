import random
r = random.randint(1, 100)
while True:
	N = input('請輸入數字：')
	N = int(N)
	if N == r:
		print('恭喜你，你猜對了')
		break
	elif N > r:
		print('太大了')
	elif N < r:
		print('太小了')