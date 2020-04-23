import pandas as pd


def load_data(file):
    if "csv" in file:
        read_file = pd.DataFrame(pd.read_csv(file))
        return read_file
    elif "xlsx" in file:
        read_file = pd.DataFrame(pd.read_excel(file))
        return read_file
    else:
        return "Cannot load file"


def retrieve_country_data(file, country, figures):
    df = load_data(file)
    df_grouped = df.groupby("Country")
    country = df_grouped.get_group(country)[figures]

    return country


# used for logistic function calculation
def a_value(confirmed_data, population):
    dN = confirmed_data.iloc[-1] - confirmed_data.iloc[0]
    dt = len(confirmed_data)
    N = confirmed_data.iloc[-1]
    N_max = population
    a = (dN/dt)/((1-N/N_max)*N)

    return a