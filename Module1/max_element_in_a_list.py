def maxCal(lists):
    mx = 0
    for num in lists:
        if num>mx:
            mx=num
    return mx

userInput = input()
lists = list(map(int,userInput.split(' ')))
print(maxCal(lists))