    for i in arr:
            if i == arr[-1]:
                print(i)
                break
            sum += i - arr.index(i + 1)
            print(i)
