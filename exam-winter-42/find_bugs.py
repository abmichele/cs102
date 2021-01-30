import typing as tp

def read_task(filename: str) -> list(str):
    result = filename.split('t')
    result.remove('')
    result1 = []
    for i in result:
        i = i[4:len(i)]
        result1.append(i)
    return result1



def corresponding(task: str) -> int:
    task = list(task)
    count_ = {a:task.count(str(a)) for a in task}
    count_.pop(' ')
    count_.pop('-')
    count_.pop('>')
    mistakes = 0
    for i in count_.values():
        if i != 2:
            mistakes += 1
    return mistakes


def switch_mistakes(task: str) -> int:
    task = list(task)
    mistakes = 0   
    if task[0] != task[-1]:
        mistakes += 1 
    for i in range(5, len(task) - 6, 7):
        if task[i] != task[i + 2]:
            mistakes += 1
    return mistakes

def find_bugs(task) -> str:
    all_mistakes = switch_mistakes(task) + corresponding(task)
    if all_mistakes > 1:
        return 'V, V, V...'
    elif all_mistakes == 1:
        return 'here'
    else:
        return 'V, V, V...'

f = str(open(*))
task = read_task(f)
for i in task:
    if find_bugs(i) == 'V, V, V...':
        print(find_bugs(i))
    elif find_bugs(i) == 'here':
        print('task'+str(i))


