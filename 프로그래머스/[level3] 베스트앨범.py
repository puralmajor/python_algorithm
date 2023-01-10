from collections import defaultdict, deque


def solution(genres, plays):
    songs = defaultdict(list)
    order = deque()
    answer = []
    for idx, cont in list(enumerate(list(zip(genres, plays)))):
        songs[cont[0]].append([idx, cont[1]])

    songs = dict(
        sorted(songs.items(), key=lambda x: sum(x[1][1]), reverse=True))

    for genre in songs.keys():
        songs[genre] = list(
            sorted(songs[genre], key=lambda x: x[1], reverse=True))

        if len(songs[genre]) > 1:
            answer.append(songs[genre][0][0])
            answer.append(songs[genre][1][0])
        else:
            answer.append(songs[genre][0][0])

    return answer


solution(["classic", "pop", "classic", "classic", "pop"],
         [500, 600, 500, 800, 2500])
