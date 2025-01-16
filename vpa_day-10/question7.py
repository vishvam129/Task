# 7. Write a Python program to add three given lists using Python map and lambda.
sample_list_1 = [1,2,3,4,5]
sample_list_2 = [1,2,3,4,5]
sample_list_3 = [1,2,3,4,5]

aded_list = map(lambda a,b,c : a+b+c ,sample_list_1,sample_list_2,sample_list_3)
print(list(aded_list))