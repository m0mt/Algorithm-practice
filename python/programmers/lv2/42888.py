def solution(record):
    answer = []
    record = [i.split(" ") for i in record]
    user = {i[1]: i[2] for i in record if i[0] in ("Enter", "Change")}

    for i in record:
        if i[0] == "Enter":
            txt = user[i[1]] + "님이 들어왔습니다."
        elif i[0] == "Leave":
            txt = user[i[1]] + "님이 나갔습니다."
        else :
            continue
        answer.append(txt)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))