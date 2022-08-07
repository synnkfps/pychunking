import time

big_list = []
list_size = 1000000
cluster = []

def results(start, end):
    return ''.join(list(str(end-start))[:6])

def create_list():
    global cluster 
    cluster = [0] * list_size
    st = time.time()
    for i in range(list_size):
        big_list.append(i)

        if len(big_list) == list_size:
            ed = time.time()
            print(f"finished writing: {results(st, ed)}s")
            break
    
chunk = []
count = 0

def iterate(vanilla = bool):
    global big_list, count, chunk, cluster
    st = time.time()
    c = 0

    for i in big_list:
        count += 1
        chunk.append(i)
        if not vanilla and count>10:
            chunk = []
            continue

        if count == len(cluster):
            ed = time.time()
            print(f"({'vanilla' if vanilla else 'chunked'}) finished reading: {results(st, ed)}s (list size: {len(cluster)})\n")
            break

def mass_clear():
    global big_list, chunk, count
    big_list.clear()
    chunk.clear()
    count = 1

# Vanilla Reading
create_list()
iterate(True)

mass_clear()

# Use Chunking
create_list()
iterate(False)
