score = 4
try:
    with open("scores.txt", 'a') as scores_file:
        scores_file.write(str(score) + "\n")

except Exception as err:
    print(err)