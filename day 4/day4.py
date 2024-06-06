import numpy as np
import pandas as pd

s = pd.Series([3, 2, np.nan, np.nan, 11, 7])
print(s)

dates = pd.date_range("20240605", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20240605"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "baa",
    }
)
print(df2)

def viewData(df):
    print(df.dtypes)         # types of data (float, integer, category...)
    print(df.head(3))        # first 3 rows
    print(df.tail(3))        # last 3 rows
    print(df.index)          # gives indexs
    print(df.columns)        # gives columns
    print(df.to_numpy())     # just data
    print(df.describe())     # gives summary of data
    print(df.T)              # rows = column, column = rows
    print(df.sort_index(axis=1, ascending=False))   # sorts by index
    print(df.sort_values(by="B"))                   # sorts by value
# viewData()

def selection(df):
    print(df["A"])                    # gets only row A and the index and type of data
    print(df[0:3])                    # gets the matching rows
    print(df["20240605":"20240608"])  # gets matching row from index 
    print(df.loc[dates[0]])           # gets a row matching a label/index
    print(df.loc[:, ["A", "B"]])      # gets data for coloumnS mentioned
    print(df.loc["20240605":"20260608", ["A", "B"]])     # gets data for index mentioned and column mentioned
    print(df.loc[dates[0], "A"])      # gets term from point
    print(df.at[dates[0], "A"])       # same thing
    print(df.iloc[3])                 # gets the row using idex at mentioned index
    print(df.iloc[3:5, 0:2])          # gets mentioned rows then mentioned columns    [row, index]
    print(df.iloc[[1, 2, 4], [0, 2]]) # selects specific rows then columns
    print(df.iloc[1:3, :])            # selects rows then all columns
    print(df.iloc[:, 1:3])            # selects columns then all rows
    print(df.iloc[1, 1])              # gets term at specific point 
    print(df.iat[1, 1])               # same thing
    print(df[df["A"] > 0])            # gets values in slected column that meets condition
    print(df[df > 0])                 # shows value that meet condition, others become NaN
    df2 = df.copy()                   # copies a data_frame
    df2["E"] = ["one", "one", "two", "three", "four", "three"]       # adds a column to the data frame
    print(df2)                        # prints new data frame
    print(df2[df2["E"].isin(["two", "four"])])            # prints rows/index where mentioned coloumn meets either condition
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20240605", periods=6))
    print(s1)                         # prints data with only index no top bar
    df["F"] = s1                      # new row "F" becomes s1 is added to df
    df.at[dates[0], "A"] = 0          # mentioned term becomes 0
    df.iat[0, 1] = 0                  # mentioned term becomes 0
    df.loc[:, "D"] = np.array([3.14] * len(df))              # all rows/index terms in coloumn mentioned becomes number before len(df), len(df) cannot be changed
    print(df)                         # print updated data_frame
    df2 = df.copy()                   # df is copied onto df2
    df2[df2 > 0] = -df2               # df2 positive terms become negative

selection(df)