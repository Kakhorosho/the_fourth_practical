frst_tm, scnd_tm = map(int, input().split(':'))
if frst_tm < scnd_tm:
    print(2)
elif scnd_tm < frst_tm:
    print(1)
else:
    print(int(scnd_tm != frst_tm))
