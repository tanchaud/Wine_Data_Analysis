import pandas as pd
import numpy as np


def get_df():
    red_wine = pd.read_csv('/Users/tanchaud/CAB_Berlin/Project_2/Sprint_1/winequality-red.csv', sep=';')


def RemoveOutliersByFeature(df=None,\
                            feature=None,\
                            in_place=False):
    if True==in_place:
        q1=df[feature].quantile(0.25)
        q3=df[feature].quantile(0.75)
        iqr=(q3-q1)
        lower=(q1-(1.5*iqr))
        upper=(q3+(1.5*iqr))
        df=df.loc[(df[feature]>=lower) & (df[feature]<=upper)]
    else:
        q1=df[feature].quantile(0.25)
        q3=df[feature].quantile(0.75)
        iqr=(q3-q1)
        lower=(q1-(1.5*iqr))
        upper=(q3+(1.5*iqr))
        df=df.loc[(df[feature]>=lower) & (df[feature]<=upper)]
        return(df)

def ImputeOutliersByFeatureReplaceByQualityLabel(df=None,\
                            feature=None,\
                            quality_label='None',\
                            in_place=False):
    """
    TODO: Preserve by label, replace outliers by mean only for other labels.
    :df             : DataFrame.
    :feature        : Feature to check distribution of in the DataFrame.
    :return: None.
    """

    if True==in_place:
        return(None)

    else:
        dummy_hqcnt=0
        q1=df[feature].quantile(0.25)
        q3=df[feature].quantile(0.75)
        iqr=(q3-q1)
        lower=(q1-(1.5*iqr))
        upper=(q3+(1.5*iqr))
        mean=df[feature].mean()
        for iter_range in range(df[feature].size):
            if df.iloc[iter_range]['quality_label']!=quality_label:
                if( (df.iloc[iter_range][feature]<=lower) or (df.iloc[iter_range][feature]>=upper)):
                    df.iloc[iter_range][feature]=mean
        return(df)





