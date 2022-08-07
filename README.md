### pychunking
prototypes of python chunk-ing (write and read big lists faster)

### 1st prototype mechanic
its simple, create an list normally, then to iterate it appends the elements of the list with a counter, if the counter is 10, clear the list and continue appending, i enjoyed it because it works as i wanted to, its also extremly fast!

times:
```py
Threaded:
Writing: 0.009538650512695312s
Reading: 0.06184983253479004s

Vanilla:
Writing: 0.25143861770629883s
Reading: 0.3879261016845703s

No Chunking
Writing: 0.20973420143127441s
Reading: 0.20973420143127441s
```
converted:

```py
Threaded:
Writing: 0.0095ms
Reading: 0.0618ms
Total: 0.0713ms

Vanilla:
Writing: 0.2514ms
Reading: 0.3879ms
Total: 0.3879ms

No Chunking
Writing: 0.2097ms
Reading: 0.2097ms
Total: 0.2097ms
```
