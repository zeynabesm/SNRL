import pandas as pd



class BenchmarkLoader:


    def load_csv(
        self,
        path
    ):

        return pd.read_csv(path)



    def split_target(
        self,
        df,
        target
    ):

        X = df.drop(
            columns=[target]
        )


        y = df[target]


        return X,y