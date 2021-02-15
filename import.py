import random
Max = input('請決定最大值:')
Max = int(Max)
Min = input('請決定最小值:')
Min = int(Min)

r = random.randint(Min, Max)
count = 0
while True:
	count = count + 1
	N = input('請輸入數字：')
	N = int(N)
	if N == r:
		print('恭喜你，你猜對了')
		print('這是你猜的第', count,'次')
		break
	elif N > r:
		print('太大了')
	elif N < r:
		print('太小了')
	print('這是你猜的第', count,'次')