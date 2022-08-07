### pychunking
prototypes of python chunk-ing (write and read big lists faster)

### 1st prototype mechanic
its simple, create an list normally, then to iterate it appends the elements of the list with a counter, if the counter is 10, clear the list and continue appending, i enjoyed it because it works as i wanted to, its also extremly fast!

times (list size = :
```py
finished writing: 0.2562s
(chunked) finished reading: 0.5703s (list size: 999999)

finished writing: 0.2460s
(vanilla) finished reading: 0.5139s (list size: 999999)
```
