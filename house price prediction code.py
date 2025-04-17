# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load and inspect data
data = pd.read_csv("data/final_data.csv")
print(data.head())
print(data.tail())
print(data.info())

# Check and handle missing values
print(data.isna().sum())

# Drop unnecessary columns
data.drop(data.columns[[0, 2, 3, 15, 17, 18]], axis=1, inplace=True)
print(data.columns)

# Convert and clean data
data['zindexvalue'] = data['zindexvalue'].str.replace(',', '').apply(pd.to_numeric)
print(data.info())

# Data summary
print(data.lastsolddate.min(), data.lastsolddate.max())
print(data.describe())

# Visualize data
data.hist(bins=50, figsize=(20, 15))
plt.savefig("Attribute_histogram_plots")
plt.show()

data.plot(kind="scatter", x="longitude", y="latitude", alpha=0.2)
plt.savefig("map1.png")

data.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, figsize=(10, 7),
          c="lastsoldprice", cmap="jet", colorbar=True, sharex=False)
plt.savefig("map2.png")

# Correlation analysis
corr_matrix = data.corr()
print(corr_matrix["lastsoldprice"].sort_values(ascending=False))

# Scatter matrix visualization
from pandas.plotting import scatter_matrix
attributes = ["lastsoldprice", "finishedsqft", "bathrooms", "zindexvalue"]
scatter_matrix(data[attributes], figsize=(12, 8))
plt.savefig("matrix.png")

data.plot(kind="scatter", x="finishedsqft", y="lastsoldprice", alpha=0.5)
plt.savefig("scatter.png")

# Feature engineering
data['price_per_sqft'] = data['lastsoldprice'] / data['finishedsqft']
print(data.corr()["lastsoldprice"].sort_values(ascending=False))

# Grouping and clustering
freq = data.groupby('neighborhood').count()['address']
mean = data.groupby('neighborhood').mean()['price_per_sqft']
cluster = pd.concat([freq, mean], axis=1)
cluster.columns = ['freq', 'price_per_sqft', 'neighborhood']

cluster1 = cluster[cluster.price_per_sqft < 756]
cluster_temp = cluster[cluster.price_per_sqft >= 756]
cluster2 = cluster_temp[cluster_temp.freq < 123]
cluster3 = cluster_temp[cluster_temp.freq >= 123]

def get_group(x):
    if x in cluster1.index:
        return 'low_price'
    elif x in cluster2.index:
        return 'high_price_low_freq'
    else:
        return 'high_price_high_freq'

data['group'] = data.neighborhood.apply(get_group)

# Prepare data for modeling
data.drop(data.columns[[0, 4, 6, 7, 8, 13]], axis=1, inplace=True)
data = data[['bathrooms', 'bedrooms', 'finishedsqft', 'totalrooms', 'usecode',
             'yearbuilt', 'zindexvalue', 'group', 'lastsoldprice']]

X = data[['bathrooms', 'bedrooms', 'finishedsqft', 'totalrooms', 'usecode', 
          'yearbuilt', 'zindexvalue', 'group']]
Y = data['lastsoldprice']

# Encode categorical variables
X = pd.concat([X, pd.get_dummies(data.group), pd.get_dummies(data.usecode)], axis=1)
X.drop(['group', 'usecode'], axis=1, inplace=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Linear Regression
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print(f'Linear Regression R^2: {reg.score(X_test, y_test):.4f}')
print(f'Linear Regression RMSE: {np.sqrt(mean_squared_error(y_pred, y_test)):.4f}')
print(f'Linear Regression MAE: {mean_absolute_error(y_pred, y_test):.4f}')

# Random Forest
forest_reg = RandomForestRegressor(random_state=42)
forest_reg.fit(X_train, y_train)
y_pred = forest_reg.predict(X_test)

print(f'Random Forest R^2: {forest_reg.score(X_test, y_test):.4f}')
print(f'Random Forest RMSE: {np.sqrt(mean_squared_error(y_pred, y_test)):.4f}')

# Gradient Boosting
model = GradientBoostingRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f'Gradient Boosting R^2: {model.score(X_test, y_test):.4f}')
print(f'Gradient Boosting RMSE: {np.sqrt(mean_squared_error(y_pred, y_test)):.4f}')

# Feature Importance
feature_labels = np.array(['bathrooms', 'bedrooms', 'finishedsqft', 'totalrooms',
                           'yearbuilt', 'zindexvalue', 'high_price_high_freq',
                           'high_price_low_freq', 'low_price', 'Apartment',
                           'Condominium', 'Cooperative', 'Duplex', 'Miscellaneous',
                           'Mobile', 'MultiFamily2To4', 'MultiFamily5Plus',
                           'SingleFamily', 'Townhouse'])
importance = model.feature_importances_
feature_indexes_by_importance = importance.argsort()

for index in feature_indexes_by_importance:
    print(f'{feature_labels[index]}: {importance[index] * 100.0:.2f}%')
