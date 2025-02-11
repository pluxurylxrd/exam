file = '1task.txt'

def analiz(file):
    res = []
    with open(file, 'r') as f:
        str_number = 1
        for line in f:
            cnt_probel = line.count(' ')
            res.append((str_number, cnt_probel))
            str_number += 1
    return res

def hash(task):
    # sum = 0
    # for str_number, cnt_probel in task:
    #     sum += (str_number * cnt_probel)
    # return sum
    return sum(str_number * cnt_probel for str_number, cnt_probel in task)

task = analiz(file)

for str_number, cnt_probel in task:
    print(f'Строка под номером {str_number} содержит {cnt_probel} пробелов')

task_hash = hash(task)

print(f'Хеш: {task_hash}')