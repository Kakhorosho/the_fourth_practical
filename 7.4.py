frst_tm, scnd_tm = map(int, input().split())
if frst_tm < scnd_tm:
    print(scnd_tm)
elif scnd_tm < frst_tm:
    print(frst_tm)
else:
    print(int(scnd_tm != frst_tm))