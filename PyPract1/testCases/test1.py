str='srikanthreddy chelukala'
freq={}
for i in str:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)
