import datetime
import re
# розпакувати архів щоб скрипт працював справно
filename = 'access_log_Jul95'
regex = re.compile('apollo-13')
time_regex = re.compile('\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}')
start = datetime.datetime.fromisoformat('1995-07-01 00:55:00')
end = datetime.datetime.fromisoformat('1995-07-01 01:25:00')

search_string = 'apollo-13'


def main():
    file = open(filename, encoding='ISO-8859-1')
    size = 0

    lines = filter(regex.search, file)
    for index, line in enumerate(lines):
        if re.search('01/Jul/1995', line):
            time = re.search(time_regex, line).group()
            time = datetime.datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')
            if start < time < end:
                size += int(line.strip().split()[-1])
    file.close()
    print(f'Total amount of apollo-13 request - {index+1}\n'
          f'Data size is {size} bytes')


if __name__ == '__main__':
    main()
