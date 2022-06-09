import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random 
import pandas as pd
import csv

df = pd.read_csv("datasets-master/datasets-master/schooldata.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)

print("Mean of sampling distribution : ",mean)
print("Standard deviation",std_deviation)

first_std_deviation_start, first_std_deviation_end= mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end= mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end= mean-(3*std_deviation), mean+(3*std_deviation)

print("std1",first_std_deviation_start,first_std_deviation_end)
print("std2",second_std_deviation_start,second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

zscore= (mean_of_sample_1-mean)/std_deviation
print("the zcore is",zscore)