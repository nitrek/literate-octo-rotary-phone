#given a string find first non-repeating character


# def first_non_repeating_char(string):
#     count = [0] * 256
#     firstchar = string[0]
#     for i in string[::-1]:
#         count[ord(i)] = count[ord(i)] + 1
#         if count[ord(i)] == 1:
#             firstchar = i

#     print(firstchar)    


# first_non_repeating_char("geeksforgeeks")



#Arrange given numbers to form the biggest number 


# def afirst(a ,b):

#     ab = int(str(a)+str(b))

#     ba = int(str(b)+str(a))

#     return True if ab < ba else False

# def swap(arr,i,j):
#     tmp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = tmp
# def largestNumber(nums):
#     i = 0
#     for i in range(0,len(nums)):
#         j = i+1
#         for j in range(0,len(nums)):
#             if(not afirst(nums[i],nums[j])):
#                 swap(nums,i,j)
#     return "".join(str(i) for i in nums)

# print(largestNumber([3,30,34,9]))


def printAnagramsTogether(words):
    groupWord = {}
    for word in words:
        if "".join(sorted(word)) in groupWord.keys():
            groupWord["".join(sorted(word))] = groupWord["".join(sorted(word))] +","+ word
        else:
            groupWord["".join(sorted(word))] = word
    return " ".join(group for group in groupWord.values())

arr =  ["cat", "dog", "tac", "god", "act"] 
print(printAnagramsTogether(arr))
