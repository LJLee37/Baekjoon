movieNum = []
current = 1
lenMovieNum = 0
while lenMovieNum < 10000:
    if "666" in str(current):
        movieNum.append(current)
        lenMovieNum += 1
    current += 1
print(movieNum[int(input()) - 1])
