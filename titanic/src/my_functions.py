import pandas as pd


# Functions
def change_dtype(dataset, dtype_list, type=None):
    """Change to correct datatype

    Args:
        dataset (DataFrame): dataset with incorrect datatype,
        dtype_list (list): list of variables you want to change the datatype of
        type (datatype): datatype to change list of variables into

    Returns:
        df (DataFrame): dataset with the correct dtypes
    """
    df = dataset.copy()
    for item in dtype_list:
        if type == None:
            df[item] = pd.to_datetime(df[item])
        else:
            df[item] = df[item].astype(type)
    return df


def descriptive_stats(df):
    """This function prints the number of unique values and number of null values for each variable.
    It also stores variables in lists if they have either a lot of unique values and/or null values

    Args:
        df (DataFrame): raw dataframe

    Returns:
        many_nulls (list): stores variables that are more than 50% null
        many_unique_vals (list): stores object data type variables that are more than 75% unique

    """
    many_unique_vals = []
    many_nulls = []

    for col in df.columns:
        print(f"{col}")
        num_unique = df[col].nunique()
        per_unique = num_unique / df.shape[0]
        print(f"Number of unique values: {num_unique} ({round(per_unique * 100, 2)}%)")

        num_null = df[col].isna().sum()
        per_null = num_null / df.shape[0]
        print(f"Number of null values: {num_null} ({round(per_null * 100,2)}%)")
        print("-----------------------------------------")
        if per_null > 0.50:
            many_nulls.append(col)
        if pd.api.types.is_numeric_dtype(df[col]) == False:
            if per_unique > 0.75:
                many_unique_vals.append(col)

    return many_nulls, many_unique_vals
