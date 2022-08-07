import time

big_list = []
list_size = 30
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
        cluster[count-1] = i
        print(cluster)
        if not vanilla and count>10:
            c += 1
            cluster.pop(count % len(big_list))
            continue

        if count == len(big_list):
            ed = time.time()
            print(f"({'vanilla' if vanilla else 'chunked'}) finished reading: {results(st, ed)}s (list size: {len(cluster)})\nTotal: {''.join(list(str(st+ed))[:6])}s")
            break

def mass_clear():
    global big_list, chunk, count
    big_list.clear()
    chunk.clear()
    count = 1


create_list()
iterate(False)

mass_clear()
