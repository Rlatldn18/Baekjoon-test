alp = input()
croalp = ['c=','c-','dz=','d-','lj','nj','s=','z='] 

for i in croalp:
    alp = alp.replace(i, "#")

print(len(alp))