import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df= employee['salary'].unique()
    df= pd.DataFrame(df,columns=['salary']).sort_values(by=['salary'],ascending=False)
    if N>len(df) or N <=0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    return df.head(N).tail(1)[['salary']].rename(columns={'salary':f'getNthHighestSalary({N})'})
   