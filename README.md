[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/3J-MMk1X)
## Problem 1. Unit Tests

Write 2 unit tests of `Circle.add_area`:

1. Typical case: Test `add_area` with two circles having positive radii.
2. Edge case: Test `add_area` when one of the circles has radius 0, 
   the other has non-zero radius. (Result should have same radius.)
   Does `add_area` work the same regardless of which circle has radius 0?

In both these cases, test that 
- the result has correct radius 
- the result has correct area

Write 1 unit test for this:

3. Circle constructor raises exception if the radius is negative.

How to test for exception?

```python
# unittest
with self.assertRaises(Explosion):
    bomb.explode()

# pytest
with pytest.raises(Explosion):
     bomb.explode()
```

## Problem 2. Doctests

Write a class docstring in the `Circle` class that includes **two** doctests.

1. Normal case. Doctest adds circles with radii 3 and 4, result has radii 5.

2. Illegal case. Doctest creates a circle with negative radius. It should raise exception.  In your doctest, use `...` to skip the stacktrace output.


## Problem 3. Write a Singleton

Use the code in the [counter](./counter) subdirectory.

1. Complete code in the `Counter` class and make it a singleton.

2. Write two unit tests to verify that it is a Singleton and that all references share the same count.  New references should **not** cause the counter to reset to zero.
