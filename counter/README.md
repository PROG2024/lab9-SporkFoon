## Singleton Counter

A Counter that is a Singleton.

Examples:
```python
counter = Counter()
counter.count
1
counter.count        # invoking count doesn't change anything
1
counter.increment()  # add 1 and return the new count
2
counter2 = Counter()
counter2 is counter
True
counter2.count       # shares same count
2
counter2.increment()  # add 1 and return the new count
3
counter.count
3
```
