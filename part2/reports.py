
# Report functions
def get_most_played(file_name):
    most_played = [0, ""]
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            if most_played[0] < float(line[1]):
                most_played[0] = float(line[1])
                most_played[1] = line[0]
    return most_played[1]

def sum_sold(file_name):
    sold = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            sold += float(line[1])
    return sold

def get_selling_avg(file_name):
    sold = 0
    games = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            sold += float(line[1])
            games += 1
    return sold / games

def count_longest_title(file_name):
    longest_title = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            if len(line[0]) > longest_title:
                longest_title = len(line[0])
    return longest_title

def get_date_avg(file_name):
    games = 0
    date_sum = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            date_sum += int(line[2])
            games += 1
    return int(round(date_sum / games))

def get_game(file_name, title):
    print(title)
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line[:-1].split("\t")
            for i in range(0, len(line)):
                if line[i].isnumeric():
                    line[i] = int(line[i])
                else:
                    try:
                        line[i] = float(line[i])
                    except Exception as e:
                        pass
            if line[0] == title:
                print(line)
                return line