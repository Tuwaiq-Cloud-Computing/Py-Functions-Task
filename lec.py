def func(x,y):
    sum=x+y
    print(sum)
func(5,5)
list=[1,2,3,4,5]
for x in list:
    print(x)
#q4
    list1=[3,1,10]
    print("largest element is",max(list1))
    #Q8
    def arrange(list2):
        for i in list2:
            if i==0:
                list2.remove(i)
                list2.append(0)
        return print(list2)
    list2=[0,1,0,0,5,7,9]
    arrange(list2)
    #Q6
    stringnum="Tuwaiq_Academy"
    for element in stringnum:
        print(element,end=' ')
        print("\n")

        #Q7
        list3=["python","c++","java"]
        for x in list3:
            if x=="c++":
                break
            print(x)















