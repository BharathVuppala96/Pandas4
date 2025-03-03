import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee['salary'].unique()
    df=pd.DataFrame(df,columns=['salary']).sort_values(by=['salary'], ascending=False)
    if len(df)<2 or len(df)==0:
        return pd.DataFrame({f'SecondHighestSalary':[None]})
    return df.head(2).tail(1)[['salary']].rename(columns={'salary':'SecondHighestSalary'})
    