file1 = open('./data/day1.txt', 'r')
lines = [line.strip() for line in file1.readlines()]


def get_all_deers():
    max_deer = 0
    cur_deer = 0
    all_deers = []
    
    for line in lines:
        if line.strip():
            cur_deer += int(line.strip())
        else:
            all_deers.append(cur_deer)
            max_deer = max(max_deer, cur_deer)
            cur_deer = 0
    return all_deers


all_deers = get_all_deers()
top_deers = sorted(all_deers, reverse=True)

print(top_deers[0])
print(sum(top_deers[:3]))
