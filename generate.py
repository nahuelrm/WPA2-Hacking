ssid = ["You are not safe", 
        "You are being watched", 
        "You are vulnerable", 
        "You should go away", 
        "run", 
        "pwned", 
        "You got hacked", 
        "Call the cops", 
        "Will never stop", 
        "Your credentials gone"]

for i in range(0,5000):
    x = i % 10
    print(i, ssid[x])

# python3 generate.py > SSID.txt
