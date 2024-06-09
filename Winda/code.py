import pandas as pd
import logicmin
df = pd.read_csv('truthtable.txt', header=None, names=['data'])

df["input"] = df["data"].str[:7]
df["output"] = df["data"].str[7:]

input_list = df["input"].values.tolist()
output_list = df["output"].values.tolist()

minimalizer = logicmin.TT(7, 7)

for i in range(len(input_list)):
    minimalizer.add(input_list[i], output_list[i])
    
solution = minimalizer.solve()

print(solution.printN(xnames = ["F1","F2","D1","D2","B0","B1","B2"],
                      ynames = ["F1'","F2'","D1'","D2'","B0'","B1'","B2'"]))
                      
                      