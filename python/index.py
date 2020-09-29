n = ["1234","2","3","4"]
m = "123"
for i in n:
    arr = [i.index(j) for j in m if j in i] 
    print(arr)  

