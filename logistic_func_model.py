# the following forecasts the state of infections in the future based on specific infection rates
from vpython import *
import pandas as pd
from a_infection import a_value, retrieve_country_data


def curve_graph(graph_number, rate_name, infection_rate, confirmed_cases, population, time):

    a = infection_rate
    n = confirmed_cases
    n_max = population
    time_period = time

    if graph_number == 1:
        infection_graph = gcurve(color=color.red, label="{} = {}".format(rate_name, a))
        t = 0
        dt = 1
        n0 = 1
        while t < time_period:
            n_old = n
            n = n + a * (1 - n / n_max) * n * dt
            r = (n - n_old) / dt

            t = t + dt

            infection_graph.plot(t, r)
    elif graph_number == 2:
        infection_graph = gcurve(color=color.blue, label="{} = {}".format(rate_name, a))
        t = 0
        dt = 1
        n0 = 1
        while t < time_period:
            n_old = n
            n = n + a * (1 - n / n_max) * n * dt
            r = (n - n_old) / dt

            t = t + dt

            infection_graph.plot(t, r)
    else:
        infection_graph = gcurve(color=color.black, label="{} = {}".format(rate_name, a))
        t = 0
        dt = 1
        n0 = 1
        while t < time_period:
            n_old = n
            n = n + a * (1 - n / n_max) * n * dt
            r = (n - n_old) / dt

            t = t + dt

            infection_graph.plot(t, r)


if __name__ == '__main__':
    # N_max
    population = 66650000

    # confirmed cases
    uk_cumulative = retrieve_country_data("/Users/YinNeoh/Downloads/COVID19Data.csv", "United Kingdom", "Confirmed")
    uk_total_infected = uk_cumulative.iloc[-1]

    # calculating the infection rate
    uk_df = retrieve_country_data("Newcases_Data.csv", "United Kingdom", "Confirmed")
    pre_lockdown = uk_df[0:61]
    avg_rate = round(a_value(uk_df, population), 3)
    pre_lockdown_rate = round(a_value(pre_lockdown, population), 3)

    graph_axes = graph(title= "How long until there are no more new infections in the UK?", xtitle="Time (days)",
                       ytitle="Number of Infections", width=1000, height=650, yscale="linear")

    curve_graph(1, "Current Rate", avg_rate, uk_total_infected, population, 1000)  # avg infection rate - red line
    curve_graph(2, "Pre-Lockdown", pre_lockdown_rate, uk_total_infected, population, 1000)  # pre-lockdown infection rate - blue line
