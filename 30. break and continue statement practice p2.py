#Add an if statement and a continue statement to the loop so that it skips when iterator equals "sun".

list =["earth","mars","sun","jupiter","pluto"]

for i in list:
    if i == "sun":
        continue
    print(i)    