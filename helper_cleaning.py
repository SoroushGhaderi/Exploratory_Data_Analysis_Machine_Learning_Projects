import pandas as pd

def standard_column_names(dataframe: pd.DataFrame):
    """
        Edit column names, remove space and replace with underline,
        then set column names lowercase -> snake_case
        
    Parameters
    ----------
    dataframe : pandas DataFrame
        DataFrame with non-standardard column names

    Returns
    -------
    dataframe : Pandas DataFrame
        Edited Dataframe with standard column names
    
    """
    return dataframe.columns.str.replace(" ", "_").str.lower()


def standard_features_string(dataframe: pd.DataFrame):
    """ 
        Edit feature names in each categotical column,
        first check each column, if that was categorical, 
        then going to remove space and replace with underline,
        then set feature names lowercase -> snake_case
        
    Parameters
    ----------
    dataframe : pandas DataFrame
        DataFrame with non-standardard feature names

    Returns
    -------
    dataframe : Pandas DataFrame
        Edited categorical columns of Dataframe with standard names
    
    """
    for column in dataframe.columns:
        if dataframe[column].dtype == "object":
            dataframe[column] = dataframe[column].str.replace(" ", "_").str.lower()
        else:
            pass
    return dataframe


def get_feature_names_mixture_column_transformer(mixture_transformer,
                                                 cat_features,
                                                 numerical_name,
                                                 categorical_name):
    """ 
        Extract all feature(column) names and return a list that contains
        all the features after transforms, length of this list is equal to
        numpy array that transformed via column transformer.
        default column tranformer -> categorical and numerical pipeline 
        with one-hot encoder and simple imputer.
        
    Parameters
    ----------
    mixture_transformer : sklearn ColumnTransformer
        full column tranformer, exactly name of column transformer object 

    cat_features : python list
        list of categorical features
        
    numerical_name : python string
        name of numerical pipeline in ColumnTransformer that we defined
    
    categorical_name : python string
        name of categorical pipeline in ColumnTransformer that we defined
            
    Returns
    -------
    flat_features : python list
        list of all features header that extract from ColumnTransformer
    
    """
    full_transformer = mixture_transformer.transformers_
    all_features = []
    for name, transformer, features in full_transformer:
        if name == numerical_name:
            all_features.append(features)
        elif name == categorical_name:
            all_features.append(transformer.named_steps["One-Hot"].get_feature_names(cat_features).tolist())
    flat_features = [item for sublist in all_features for item in sublist]
    return flat_features