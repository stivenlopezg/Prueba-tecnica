import os
import pandas as pd

input_files = os.listdir('data/')


def concatenate_data(input_files: list, word: str) -> pd.DataFrame:
    files = [i for i in input_files if i.startswith(word)]
    raw_data = [pd.read_csv(f'data/{file}', sep=';', encoding='ISO-8859-1') for file in files]
    df = pd.concat(raw_data, axis=0)
    df.columns = [i.lower().replace(' ', '_') for i in df.columns]
    return df


def export_data(df: pd.DataFrame, filename: str):
    return df.to_csv(filename, sep=';', index=False)


if __name__ == '__main__':
    estado = concatenate_data(input_files=input_files, word='ESTADO')
    export_data(df=estado, filename='data/estado_tc.csv')
    trx = concatenate_data(input_files=input_files, word='TRX')
    export_data(df=trx, filename='data/trx.csv')
    info = concatenate_data(input_files=input_files, word='SIS')
    export_data(df=info, filename='data/info_sociodemografica.csv')
