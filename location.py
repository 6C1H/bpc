from ipdata import ipdata
apikey = '51aa3b542280ba0a6499f23414957c06e22f18def184ea2d48a92d75'
ip = ipdata.ipdata(apikey=apikey)
data = ip.lookup('1.1.1.1')

if data['status'] == 200:
    for key in data['response']:
        print('#', key, ':', data['response'][key])
else:
    print(data['response'])
