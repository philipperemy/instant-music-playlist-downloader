import editdistance
from tqdm import tqdm

# cat *.txt | awk '{print tolower($0)}' | sort | uniq > unique.txt

with open('unique.txt', 'r', encoding='utf8') as r:
    lines = r.read().strip().split('\n')

radius = 20  # already sorted.
editdistance_discard_threshold = 3
num_lines = len(lines)
marked_as_delete = [0] * num_lines
for i in tqdm(range(num_lines)):
    for j in range(i, min(i + radius, num_lines)):
        if i != j and editdistance.eval(lines[i], lines[j]) <= editdistance_discard_threshold:
            marked_as_delete[j] = 1

with open('unique_2.txt', 'w', encoding='utf8') as w:
    for k in range(len(marked_as_delete)):
        if not marked_as_delete[k]:
            w.write(lines[k])
            w.write('\n')
            w.flush()
