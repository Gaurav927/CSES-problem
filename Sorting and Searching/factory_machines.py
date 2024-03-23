if __name__ == '__main__':
	n, t = list(map(int, input().split()))
	times = list(map(int, input().split()))

	def check(mid):
		return sum([mid//time for time in times])>=t 

	low, high = 0, times[0]*t
	ans = None

	while (high>=low):
		mid = low + (high - low)//2

		if check(mid):
			ans = mid
			high = mid - 1
		else:
			low = mid + 1
	print(ans)



