import sqlalchemy
import pandas as pd
import os

from .config import dev_config

def main():
    config = dev_config

    dbschema_wanted= input("Enter name of the wanted schema: ");
    dbschema = dbschema_wanted + ",public"
    table_name = input("Enter table_name(default : same as schema name): ")
    if not table_name:
        table_name = dbschema_wanted

    connection = sqlalchemy.create_engine(
        f"postgresql://{config.username}:{config.password}"
        f"@{config.host}:{config.port}"
        f"/{config.db_name}",
        connect_args={'options': f'-csearch_path={dbschema}'}
    )
        

    connection.connect()

    file_name = input("Enter file path with extension: ")
    
    if '.xlsx' in file_name:
        df = pd.read_excel(file_name)
    elif '.csv' in file_name:
        delimiter = input("Enter delimiter of the file (default:,):")
        if not delimiter:
            delimiter = ','
        df = pd.read_csv(file_name, delimiter=delimiter)
    elif '.json' in file_name:
        df = pd.read_json(file_name)
    else:
        raise NotImplementedError("None implemented error")

    # dtypedict = {}
    # for i,j in zip(df.columns, df.dtypes):
    #     if "object" in str(j):
    #         dtypedict.update({i: sqlalchemy.types.String})                   
    #     elif "datetime" in str(j):
    #         dtypedict.update({i: sqlalchemy.types.DateTime})
    #     elif "float" in str(j):
    #         dtypedict.update({i: sqlalchemy.types.FLOAT})
    #     elif "int" in str(j):
    #         dtypedict.update({i: sqlalchemy.types.INT})
    #     else:
    #         raise NotImplementedError("column type not handled")

    df.to_sql(
        table_name,
        connection,
        if_exists='replace'
    )

## Comand line setup