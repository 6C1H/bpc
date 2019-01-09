import wmi
c = wmi.WMI(find_classes=False)
for i in c.Win32_Process(["Caption", "ProcessID"]):
    print(i)
