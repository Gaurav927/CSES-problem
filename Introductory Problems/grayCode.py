if __name__ == '__main__':
    n = int(input())

    def helper(n):
        if n == 1:
            return [1, 0]
        sol = [0, 1, 3, 2]
        for i in range(3, n+1):
            addition = 2**(i-1)
            temp = [addition + ele for ele in sol]
            sol = sol + temp[::-1]

        return sol

    for ele in helper(n):
        binary = list(bin(ele)[2:])
        finalRepr = [0]*(n-len(binary)) + binary
        print(''.join(str(ele) for ele in finalRepr))