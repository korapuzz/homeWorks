def count_tasks(num):
    res = "задач"
    if num % 10 == 1 and num % 100 != 11:
        res = "задача"
    elif num % 10 in (2,3,4) and num % 100 not in (12,13,14):
        res = "задачи"
    return res

team1_num = 5
team2_num = 6
name_1 = "Мастера кода"
name_2 = "Волшебники данных"
score_1 = 40
score_2 = 41
team1_time = 1552.512
team2_time = 2153.31451
time_avg = 45.2

tasks_total = score_1 + score_2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f"победа команды {name_1}!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f"победа команды {name_2}!"
else:
    challenge_result = "пичья!"

# Использование %:
print("В команде %s участников: %s ! " %(name_1, team1_num))
print("Итого сегодня в командах участников: %s и %s !" %(team1_num, team2_num))

# Ииспользование format():
print("Команда {} решила задач: {} !".format(name_1, score_2))
print("{} решили задачи за {} с !".format(name_1, team1_time))
print("{} решили задачи за {} с !".format(name_2, team2_time))

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")

print(f"Результат битвы: {challenge_result}")
count_text = count_tasks(tasks_total)
print(f"Сегодня было решено {tasks_total} {count_text}, в среднем по {time_avg} секунды на задачу!.")
