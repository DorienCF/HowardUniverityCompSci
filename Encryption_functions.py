import math
def MESS_Encrypt(message,Hour,Minute,Secconds):
    #hour  = datetime.utcnow().hour; minit = datetime.utcnow().minute; sec = datetime.utcnow().seccond
    long=5219283133417550597608921138394131714748003987111696388844721857021695621345566328693730284546120701185550350229748838662252951341253421746795 # long prime number used later
    #print(f'Time test\t Hour:{hour}\tMinute:{minute}\tsec:{seccond}')
    
    def upsil(long,data):
        DaTa = str(data)
        LoNg = str(long)
        Lendata= len(DaTa)
        Upsilo = LoNg[1:Lendata]
        return Upsilo
    def delt(Hour,Secconds, Upsilon):
        deltaa =  int(Upsilon) * math.sqrt(Hour*Secconds)
        return deltaa
    def sig(Hour,Minute, Upsilon):
        sigm =  int(Upsilon) * math.sqrt(Minute*Secconds)
        return sigm
    Upsilon = upsil(long, message)
    delta = int(delt(Hour,Secconds,Upsilon))
    sigma = int(sig(Hour,Minute,Upsilon))
    theta = "+"
    def symetric_encrypt(data,theta, delta, sigma):
        if theta == "+":
            EnC = data^2 + delta * sigma
        elif theta == "*":
            EnC = data^2 * delta * sigma
        else:
            print("Theta Error")    
        return EnC
    return symetric_encrypt(message,theta,delta,sigma)


def RSA_Encrypt(message):
    def lcm(a,b):
        return abs(a*b)//math.gcd(a,b)
    p = 11; Q = 7; n = p * Q 
    lam_n = lcm(p-1,Q-1) # this number should be: 30
    e = 19
    d = e %n
    
    c = message^e%n
    return c

def MESS_Decrypt(message,Hour,Minute,Secconds):
    #hour  = datetime.utcnow().hour; minit = datetime.utcnow().minute; sec = datetime.utcnow().seccond
    long=5219283133417550597608921138394131714748003987111696388844721857021695621345566328693730284546120701185550350229748838662252951341253421746795 # long prime number used later
    #print(f'Time test\t Hour:{hour}\tMinute:{minute}\tsec:{seccond}')
    
    def upsil(long,data):
        DaTa = str(data)
        LoNg = str(long)
        Lendata= len(DaTa)
        Upsilo = LoNg[1:Lendata]
        return Upsilo
    def delt(Hour,Secconds, Upsilon):
        deltaa =  int(Upsilon) * math.sqrt(Hour*Secconds)
        return deltaa
    def sig(Hour,Minute, Upsilon):
        sigm =  int(Upsilon) * math.sqrt(Minute*Secconds)
        return sigm
    Upsilon = upsil(long, message)
    delta = int(delt(Hour,Secconds,Upsilon))
    sigma = int(sig(Hour,Minute,Upsilon))
    theta = "+"
    def symetric_encrypt(data,theta, delta, sigma):
        if theta == "+":
            EnC = (math.sqrt(data)) - (delta/sigma)
        elif theta == "*":
            EnC = (math.sqrt(data)) / (delta/sigma)
        else:
            print("Theta Error")    
        return EnC
    return symetric_encrypt(message,theta,delta,sigma)


def RSA_Decrypt(message):
    def lcm(a,b):
        return abs(a*b)//math.gcd(a,b)
    p = 11; Q = 7; n = p * Q 
    lam_n = lcm(p-1,Q-1) # this number should be: 30
    e = 19
    d = e %n
    
    pt = message^d %n
    return pt
   