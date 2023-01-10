def solution(survey, choices):
    mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(survey):
        score = choices[i] - 4
        if score < 0:
            mbti[survey[i][0]] += -score
        else:
            mbti[survey[i][0]] += score
    print(mbti)
    answer = ''
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

solution(survey, choices)