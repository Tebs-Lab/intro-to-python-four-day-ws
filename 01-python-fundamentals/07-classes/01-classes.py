# Classes are a form of complex data that combines data and functions.
# ML Libraries frequently provide classes as one of the main features, 
# where each model is a class that has an internal state as well as some
# useful functions for fitting/training the model and using it to make
# predictions.


# Classes are used throughout the programming industry, not just by ML
# folks.

# Note, for a version of this class with proper "doc strings" and many more comments
# see the supplemental folder.

class SimpleLinearRegression:
    # Note, all methods should take "self" as the first parameter.
    # This has to do with how Python implements classes. The first
    # passed parameter is always a reference to the current instance
    # of this class and the name is always "self" by convention.
    
    def __init__(self):
        # Within methods of the class, the keyword 'self' refers to the 
        # particular instance of the class — in this case it's the instance
        # that we are creating in the constructor.
        self.slope = None
        self.y_intercept = None
    

    def fit(self, x_points, y_points):
        # It's common to check that the input is valid, and raise an
        # exception if the caller made a mistake.
        if len(x_points) != len(y_points):
            raise ValueError("There must be the same number of x and y data points.")

        x_mean = sum(x_points) / len(x_points)
        y_mean = sum(y_points) / len(y_points)

        x_variance = 0.0
        covariance = 0.0
        for x, y in zip(x_points, y_points):
            covariance += (x - x_mean) * (y - y_mean)
            x_variance += (x - x_mean)**2
        
        # Note: now we are setting the properties on self
        # that we created in the constructor
        self.slope = covariance / x_variance
        self.y_intercept = y_mean - (self.slope * x_mean)


    def predict(self, x):
        return (self.slope * x) + self.y_intercept


# When we want to use a class, we invoke the constructor using the 
# name of the class.
linear_model = SimpleLinearRegression()

# We've created a unique data type!
print(type(linear_model)) # <class '__main__.SimpleLinearRegression'>

# We need some data to fit our linear model...
# Here is some very simple toy data that has
# perfect covariance to test our model...
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Calling a method is done using dot notation.
linear_model.fit(x_values, y_values)

# We can access the properties of an object this way too
print(linear_model.slope, linear_model.y_intercept) # 2, 0

# Using our predict method...
prediction = linear_model.predict(3.45)
print(prediction)

# Micro-exercise: Create a second instance of the SimpleLinearModel class
# then create two new lists of x and y data and fit the model on that data.
# Then, print the slope and y_intercept of your model, and use it to make a
# prediction for some made up x point.
