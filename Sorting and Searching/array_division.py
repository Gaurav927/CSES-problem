if __name__ == '__main__':
	n, k = list(map(int, input().split()))
	arr = list(map(int, input().split()))

	if k==1:
		print(sum(arr))

	elif k==n:
		print(max(arr))
	else:
		def check(mid):
			count = 1
			total = 0

			for i in range(n):
				total = total + arr[i]
				if arr[i]>mid:
					return False
				if total>mid:
					count += 1
					total = arr[i]

			return count<=k

		high = sum(arr)
		low = 0
		ans = None


		while (high>=low):
			mid = low + (high - low)//2

			if check(mid):
				ans= mid
				high = mid - 1
			else:
				low = mid + 1
		print(ans)