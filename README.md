### pychunking
prototypes of python chunk-ing (write and read big lists faster)

### 1st prototype mechanic
its simple, create an list normally, then to iterate it appends the elements of the list with a counter, if the counter is 10, clear the list and continue appending, i enjoyed it because it works as i wanted to, its also extremly fast!

times:
```py
finished writing: 3.9249s
(vanilla) finished reading: 3.4259s (list size: 9999999)

finished writing: 3.5769s
(chunked) finished reading: 4.4810s (list size: 21) # chunk size
```
