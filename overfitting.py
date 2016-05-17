import numpy                   as np
import pandas                  as pd
import statsmodels.formula.api as smf

print('np.dtype is {}'.format(np.dtype))

from sklearn.metrics import mean_squared_error

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)

train_X, train_y = X[:700], y[:700]
test_X, test_y = X[700:], y[700:]

train_df = pd.DataFrame({'X': train_X, 'y': train_y})
test_df = pd.DataFrame({'X': test_X, 'y': test_y})

# Linear Fit
poly_1 = smf.ols(formula='y ~ 1 + X', data=train_df).fit()

# Quadratic Fit
poly_2 = smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()

def f1(x):
    return (0.8896 * x) + 1.9959

def f2(x):
    return (0.0627 * x * x) + (0.2313 * x) + 3.1458

print('test_X.dtype is {}'.format(test_X.dtype))

y_pred1 = map(f1, test_X)
y_pred2 = map(f2, test_X)

print('mse for linear model is {}'.format(mean_squared_error(test_y, y_pred1)))
print('mse for 2nd order model is {}'.format(mean_squared_error(test_y, y_pred2)))
