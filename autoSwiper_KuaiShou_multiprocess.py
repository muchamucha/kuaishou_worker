import os
devices=os.popen('adb devices').read()
# print(devices)
sr_n=[]
filters=['list','of','device','devices','attached','unauthorized']
for item in devices.split():
    print(item)
    if item.lower() not in filters:
        sr_n.append(item)
print(sr_n)