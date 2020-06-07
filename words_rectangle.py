def rect_frame(element_list):
    length=max(len(i) for i in element_list)
    print("*"*(length+4))
    for i in element_list:
        print("*"+" "+i+" "*((length+4)-len(i)-3)+"*")
    print("*"*(length+4))
	
n=int(input("Enter the number of words"))
list1=[]
for i in range(0,n):
    word=input("Enter the word")
    list1.append(word)
rect_frame(list1)

