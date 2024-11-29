def count_calls ():
    global calls
    calls += 1
    return calls

def string_info(line):
    count_calls()
    return (len(line), line.upper(), line.lower())


def is_contains(line, lines):
    lowercase_list = [s.lower() for s in lines]
    count_calls()
    rez = True if line.lower() in lowercase_list else False
    return rez

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
