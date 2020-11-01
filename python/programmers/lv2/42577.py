def solution(phone_book):
    n = len(phone_book)
    phone_book.sort(key=lambda x : len(x))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if phone_book[j].find(phone_book[i]) == 0:
                return False 
    return True

def solution1(phone_book):
    for phone1 in phone_book:
        for phone2 in phone_book:
            if phone1 != phone2 and phone2.find(phone1) == 0:
                return False
    return True

print(solution(["119","97674223","1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))