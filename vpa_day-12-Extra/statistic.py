import statistics    
datasets = [5, 2, 7, 4, 2, 6, 8]     
x = statistics.mean(datasets)     
print("Mean is :", x)
print("Median of data-set is : ",(statistics.median(datasets))) 
print("Calculated Mode is : ",(statistics.mode(datasets)))
print("Standard Deviation of sample is :", (statistics.stdev(datasets)))
print("Low median of data-set is :",(statistics.median_low(datasets)))
print("High median of data-set is :",(statistics.median_high(datasets)))  