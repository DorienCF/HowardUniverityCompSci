import math

class Encrypt():
    #hour  = datetime.utcnow().hour; minit = datetime.utcnow().minute; sec = datetime.utcnow().seccond
     # long prime number used later
    #print(f'Time test\t Hour:{hour}\tMinute:{minute}\tsec:{seccond}')
    def upsil(data,long):
        DaTa = str(data)
        LoNg = str(long)
        Lendata= len(DaTa)
        Upsilo = LoNg[1:Lendata]
        return Upsilo
    def delt(Hour,Secconds, Upsilon):
            deltaa =  int(Upsilon) * (math.sqrt(Hour) * math.sqrt(Secconds))
            return int(deltaa)
    def sig(Secconds,Minute, Upsilon):
            sigm =  int(Upsilon) * (math.sqrt(Minute) * math.sqrt(Secconds))
            return int(sigm)
    def symetric_encrypt(data,theta, delta, sigma):
            if theta == "+":
            #print(delta,sigma,data)
                EnC = data^2 + delta * sigma
            elif theta == "*":
                EnC = data^2 * delta * sigma
            else:
                print("Theta Error")    
            return EnC
    def RSA_Encrypt(message):
            def lcm(a,b):
                return abs(a*b)//math.gcd(a,b)
            p = 11; Q = 7; n = p * Q 
            #lam_n = lcm(p-1,Q-1) # this number should be: 30
            e = 19
            d = e %n
            
            c = message^e%n
            return c

class Decrypt():
    #hour  = datetime.utcnow().hour; minit = datetime.utcnow().minute; sec = datetime.utcnow().seccond
     # long prime number used later
    #print(f'Time test\t Hour:{hour}\tMinute:{minute}\tsec:{seccond}')
    def symetric_decrypt(data,theta, delta, sigma):
        if theta == "+":
            EnC = math.sqrt(data) - (delta/sigma)
            return EnC
        elif theta == "*":
            EnC = (math.sqrt(data)) / (delta*sigma) # doesn't get used since theta is hardcoded and not dynamic
            return EnC
        else:
            print("Theta Error")    
        

    def RSA_Decrypt(message):
        def lcm(a,b):
            return abs(a*b)//math.gcd(a,b)
        p = 11; Q = 7; n = p * Q 
        #lam_n = lcm(p-1,Q-1) # this number should be: 30
        e = 19
        d = e %n
        
        pt = message^d %n
        return pt
    