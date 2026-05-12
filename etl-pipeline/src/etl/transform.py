def transform(data):

    for name in data:
        df = data[name]
        columns = df.columns.tolist()
        for column in columns:
            print(df[column])
            print("\n")
    return True
