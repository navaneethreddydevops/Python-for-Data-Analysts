
Below snippets can be directly done in ipython
```
%%bash
uname -a
df -h

```
%%writefile print_time.py
#!/usr/bin/env python
import datetime
print(datetime.datetime.now().time())
```