H,M=map(str,input().split(":"))
if(int(H)<24 and int(M)<60):
    if(int(H)>12):
        d=int(H)-12
        if(d<10):
            print('0'+str(d)+':'+M,"PM")
        else:
             print(str(d)+':'+M,"PM")
    elif(int(H)==12):
        print("12:"+M,"PM")
    elif(H=='00'):
        print("12:"+M,"AM")
    elif(int(H)<12):
        print(H+":"+M,"AM")
else:
    print("-1")
