import time

big_list = []
list_size = 10000000

def results(start, end):
    return ''.join(list(str(end-start))[:6])

def create_list():
    st = time.time()
    for i in range(list_size):
        big_list.append(i)

        if len(big_list) == list_size:
            ed = time.time()
            print(f"finished writing: {results(st, ed)}s")
            break
    
chunk = []
count = 1

def iterate(vanilla = bool):
    global big_list, count, chunk, cluster
    st = time.time()
    current = 1
    
    for i in big_list:
        current += 1
        chunk.append(i)
        
        if not vanilla and len(chunk)>100:
            current += 1
            chunk = []
            continue

        if current == list_size:
            ed = time.time()
            print(f"({'vanilla' if vanilla else 'chunked'}) finished reading: {results(st, ed)}s (list size: {len(chunk)})\n")
            break

def mass_clear():
    global big_list, chunk, count
    big_list.clear()
    chunk.clear()
    count = 1


create_list()
iterate(True)

mass_clear()

create_list()
iterate(False)

mass_clear()
