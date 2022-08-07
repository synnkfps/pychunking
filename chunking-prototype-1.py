import threading, time

big_list = []
count1 = 1

list_size = 999999

def create_list():
    #start = time.time()
    for i in range(list_size):
        big_list.append(i)
        if len(big_list) == list_size:
            #end = time.time()
            #print(f'Created List in {float(end-start)}s')
            break
        

chunk = []
count = 1

def iterate():
    global big_list
    global count 
    global chunk

    start = time.time()

    for i in big_list:
        count += 1
        chunk.append(i)
        if len(chunk)>10:
            chunk = []
            continue

        if count == len(big_list):
            #end = time.time()
            #print(f'Finished iterating in {end - start}     List size: {len(big_list)} | Chunk size: {len(chunk)}')
            break


for i in range(1,2):
    s = time.time()
    threading.Thread(target=create_list).start()
    e = time.time()
    print(f'\nThreaded:\nWriting: {e-s}s')

    s2 = time.time()
    threading.Thread(target=iterate).start()
    e2 = time.time()
    print(f'Reading: {e2-s2}s')

s = time.time()
create_list()
e = time.time()
print(f'\nVanilla:\nWriting: {e-s}s')

s2 = time.time()
iterate()
e2 = time.time()
print(f'Reading: {e2-s2}s')

s3 = time.time()

count = 0
big_list = []

for i in range(list_size):
    big_list.append(i)

e3 = time.time()
print(f'\nNo Chunking\nWriting: {e3-s3}s')

s4 = time.time()
chunk = []

for i in big_list:
    chunk.append(i)

e4 = time.time()
print(f'Reading: {e3-s3}s\n')
