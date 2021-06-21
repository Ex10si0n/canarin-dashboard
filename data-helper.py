f = open('data.csv', 'r')

saved = ''
cnt = 0

while True:
    line = f.readline()
    if ',,' in line:
        cnt += 1
        print(1)
        continue
    else:
        print(2)
        saved += line
