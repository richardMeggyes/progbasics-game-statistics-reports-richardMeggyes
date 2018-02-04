
# Report functions
file_name = "game_stat.txt"

def count_games(file_name):
    with open(file_name, 'r') as f:
        return len(f.readlines())

def decide(file_name, year):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            if line[2] == str(year):
                return True
        return False

def get_latest(file_name):
    latest_game_info = [0, ""]
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            if int(line[2]) > latest_game_info[0]:
                latest_game_info[0] = int(line[2])
                latest_game_info[1] = line[0]
    return latest_game_info[1]

def count_by_genre(file_name, genre):
    count = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            if line[3] == genre:
                count += 1
    return count

def get_line_number_by_title(file_name, title):
    counter = 1
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            if line[0] == title:
                return counter
            counter += 1

def sort_abc(file_name):
    titles = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split("\t")
            titles.append(line[0])
    titles.sort()
    return titles

