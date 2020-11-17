def solution(m, musicinfos):
    # C, C#, D, D#, E, F, F#, G, G#, A, A#, B
    answer = '(None)'
    m = replaceCode(m)
    musicinfos = [musicinfo.split(',') for musicinfo in list(map(replaceCode, musicinfos))]
    save_minute = 0
    for i in musicinfos:
        t1 = list(map(int,(i[0].split(":"))))
        t2 = list(map(int,(i[1].split(":"))))
        minute = (t2[0] - t1[0]) * 60 + t2[1] - t1[1]

        n = len(i[3])
        melody = i[3] * (minute // n) + i[3][:minute % n]
        # 조건이 일치하는게 많을 경우 , 재생시간이 긴걸로 호출
        if m in melody and save_minute < minute:
            save_minute = minute
            answer = i[2]
    return answer

def replaceCode(s):
    s = s.replace("C#","c")
    s = s.replace("D#","d")
    s = s.replace("F#","f")
    s = s.replace("G#","g")
    s = s.replace("A#","a")
    return s
    
print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
