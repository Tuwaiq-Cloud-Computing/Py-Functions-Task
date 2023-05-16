list =[1,2,3,4]
    # Question 1: Write a function that takes two numbers and return their sum
def func1(a,b):
    return a+b;

    # Question 2: Prints all the elements in the list using a for loop
def func2():
    for n in list:
        print(n);

    # Question 3: Write a Python program to sum all the items in the list
def func3():
    sum=0;
    for n in list:
        sum+=n;
    return sum;

    # Question 4: Write a Python program to get the largest number from the list
def func4():
    list.sort();
    return list[-1];

    # Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
def func5(list , num):
    n=list.index(num)
    return list[0:n+1];

    # Question 6: Loop through the letters in the string: "Tuwaiq_Academy

def func6():
    for n in "Tuwaiq_Academy":
        print(n);

    # Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
def func7():
    list = ["Python", "C++", "Java"]
    for n in list:
        if n == "C++":
            break;
        print(n)

    # Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

def func8(list):
    numOfZeros = list.count(0);
    for x in range(numOfZeros):
        list.remove(0);
    list.sort();
    for x in range(numOfZeros):
        list.append(0);
    return(list)

            


print(func1(1,4));
func2();
print(func3())
print(func4())

print(func5([4,6,3,2,7,1],2))

func6()
func7()

print(func8([4,6,0,3,1,0,2,0,8]))

# Additional Challenge:
# Build a phone book program that receives the phone number, and returns the name of the owner. You can follow the table below:

contactTable=[{"name":"Ahmed","number":"0551112222"},
         {"name":"Saad","number":"0551113333"},
         {"name":"Sultan","number":"0551114444"},
         {"name":"Morad","number":"0551115555"},
         {"name":"Abdullah","number":"0551116666"},]

search=input("Enter the phone number:")

if len(search)!= 10 and not search.isnumeric():
    print("This is invalid number")
else:
    for n in contactTable:
        if n["number"] == search:
            print(n["name"]);
            break;
    else:
        print("Sorry, the number is not found")
