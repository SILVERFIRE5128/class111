import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random 
import pandas as pd
import csv

df = pd.read_csv("datasets-master/datasets-master/studentMarks.csv")
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

df = pd.read_csv("datasets-master/datasets-master/data1.csv")
data = df["Math_score"].tolist()
mean_of_sample_1= statistics.mean(data)
print("mean_of_sample_1",mean_of_sample_1)

fig = ff.create_distplot ([mean_list],["studentMarks"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.19999],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_1,mean_of_sample_1],y=[0,0.19999],mode="lines",name="Mean of sample"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.19999],mode="lines",name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.19999],mode="lines",name="Standard Deviation 3 end"))
fig.show()

zscore= (mean_of_sample_1-mean)/std_deviation
print("the zcore is",zscore)

df = pd.read_csv("datasets-master/datasets-master/data2.csv")
data = df["Math_score"].tolist()
mean_of_sample_2= statistics.mean(data)
print("mean_of_sample_2",mean_of_sample_2)

fig = ff.create_distplot ([mean_list],["studentMarks"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.19999],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_2,mean_of_sample_2],y=[0,0.19999],mode="lines",name="Mean of sample"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.19999],mode="lines",name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.19999],mode="lines",name="Standard Deviation 3 end"))
fig.show()

zscore2= (mean_of_sample_2-mean)/std_deviation
print("the zcore is",zscore2)

df = pd.read_csv("datasets-master/datasets-master/data3.csv")
data = df["Math_score"].tolist()
mean_of_sample_3= statistics.mean(data)
print("mean_of_sample_3",mean_of_sample_3)

fig = ff.create_distplot ([mean_list],["studentMarks"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.19999],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_3,mean_of_sample_3],y=[0,0.19999],mode="lines",name="Mean of sample"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.19999],mode="lines",name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.19999],mode="lines",name="Standard Deviation 3 end"))
fig.show()

zscore3= (mean_of_sample_3-mean)/std_deviation
print("the zcore is",zscore3)