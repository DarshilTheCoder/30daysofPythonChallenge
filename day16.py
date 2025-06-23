#Today I am learning about iterator and generator! We know that using for loop we can iterate through a list or array etc, but ever wonder what happens internally, here's I am telling. Loop using an iter method, which is there in the list only, which you can see by dir(a) and loop internaly converts list into a list iterator object and it have next method through which we get the next output. 


a = ['darshil','is','nice','person']
b = range(1,5)
for i in a:
    print(i)
for i in b:
    print(i)
print(f"here in list you can see __iter__ ----->{dir(a)}'\n'") 
print(f"here in range you can see __iter__ ----->{dir(b)}'\n'")
itr_a = iter(a)
print(f"First check the type of list is ---->{type(a)}")
print(f"now see the type of list it gets converted into list iterator{type(itr_a)}")
print(f"Now here you can see the __next__ method ---->{dir(itr_a)}")

#Now I am learning generators, where I understand the when I am using return statement it returns the value and then destroy all local variables, whereas yield preserves the last state execution

#Now I understand that if you want to loop over a user-defined function or want to return only one value at a time then you need to use generator over iterator approach, why because return statement destroy the variable once value gets returned and need to send everything in one shot whearas yeild is an alternative which can preserve the last state of excution and it converts a iterator function into generator.

def rannge():
    i = 1
    while True:
        # return i 
        yield i
        i+=1

for i in rannge():
    if i >10:
        break
    print(i)