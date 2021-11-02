
if __name__=='__main__':

    t = input()

    pal = [0]*len(t)

    count = {}

    for char in t:
        count[char] = count.get(char, 0) + 1
    
    odd = 0
    for ele in count:
        if count[ele]%2:
            odd+=1
    
    if odd>1:
        print("NO SOLUTION")
    else:
        left, right = 0, len(t) - 1
        odd_element = None

        for ele in count:
            if count[ele]%2==0:
                while count[ele]:
                    pal[left] = ele
                    pal[right] = ele
                    left+=1
                    right-=1
                    count[ele]-=2
            else:
                odd_element = ele

        
        if odd_element:
            while left<=right:
                pal[left] = odd_element
                pal[right] = odd_element

                left +=1
                right-=1

        print("".join(ele for ele in pal))

