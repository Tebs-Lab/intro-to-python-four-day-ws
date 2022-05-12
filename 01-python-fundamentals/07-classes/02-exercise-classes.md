# Exercise: Using Functions and Classes

This exercise is meant to help you practice:

* Creating classes, instantiating objects, and using those objects.

# The Exercise

You will be writing a python script that create classes, then uses those classes.

> Hint: some of Python's built in functions may help you write this code faster. See: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

**Be sure to test your code with more than just this single test case!**

> Hint: Consider using the `sorted` built in function.
> Hint: You can determine if a list has an even number of items with `is_even = len(numbers) % 2 == 0`. See: [The modulo operator](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)

## Part 2: Classes

Now we're going to take the two functions you created and turn them into a class! Consider this incomplete class stub:

```python
class Averages:
    def __init__(self, input_data):
        pass # replace with your code

    def mean(self):
        pass # replace with your code

    def median(self):
        pass # replace with your code
```

Create a new python file and, using the code you wrote in part one, complete this class stub such that:

* When you create a new instance of the `Averages` class the input_data is copied and stored on `self.data`. Hint, there are [several ways to make a copy](https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list). 
* When a user calls the mean and median methods, the appropriate value is returned.

Example use, when your class is complete you should be able to use it as follows:

```python
avgs = Averages([5,10,15])
print(avgs.mean()) # 10
print(avgs.median()) # 10
```

## Reminder, The Definition of Mean and Median:

Incase you're not familiar with the concepts of the Mean and Median from statistics, they are defined as:

### Mean

The mean is the sum of the values divided by the number of values. 

**Be sure to test your code with more than just this single test case!**

> Hint: consider using the `sum` and `len` built in functions...

### Median

The median is the value at the center of the sorted dataset. If there are an even number of values in the dataset the median is the mean of the two center values.