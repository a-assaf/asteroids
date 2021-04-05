import math
import matplotlib.pyplot as plt
import numpy as np
while True:
    def main ():
        Semimajoraxis = float(input("What is the semi major Axis (a)? "))
        Period = 0.0
        eccentricity = float(input("What is the eccentricity of the orbit? "))
        loopcount = int(input("How many iterations do you want?"))
        #mu = float(input("What is the sum of the two masses? "))
        mu = float(input("What is the value of mu? "))
        n = 0.0                     
        n = math.pow(mu, .5) * math.pow(Semimajoraxis, -1.5)
        print ("n = ",n)
        Period = (2*math.pi)/n
        print ("period = ",Period)
        trate = Period/(loopcount)
        print("a = ", Semimajoraxis, "  ", "e = ", eccentricity, "  ", "mu = ", mu, "  ", "Period = ", Period, file = open("ephem.txt", "w"))
        tlist = []
        rlist = []
        flist = []
        Elist = []
        xlist = []
        ylist = []
        for j in range(loopcount):
            t = 0.0
            t = trate*j
            #print('t = ',t)
            tlist.insert(0,t)
            M = 0.0
            M = n * (t)
            #print ("M = ",M)
            #graphing M to find E
            x = np.arange(0, 4*(np.pi), 0.005)
            y = (x) - eccentricity*np.sin(x) - M
            plt.plot(x,y)
            #plt.show()
            #finds y intercepts
            E = 0.0
            xintercept = []
            for x, y in zip(x, y):
                if y < 0.01 and y > -0.01:
                    #print(x, y)
                    xintercept.insert(0,x)
            #print (xintercept)
            E = np.median(xintercept)
            #print('E = ', E)
            Elist.insert(0,E)
            r = 0.0
            r = Semimajoraxis * (1-eccentricity*math.cos(E))
            rlist.insert(0,r)
            #print ("r  = ", rlist[0])
            #finding fs
            f = 0.0
            C = 0.0
            B = 0.0
            C = math.sqrt((1 + eccentricity)/(1-eccentricity))
            B = C * math.tan(E/2)
            f = 2 * math.atan(B)
            if f<0:
                f = f+2*(np.pi)
            flist.insert(0,f)
            #print ("angle from perihelion =", flist[0])
            xvalue = 0.0
            xvalue = r * np.cos(f)
            xlist.insert(0,xvalue)
            y = 0.0
            y = r * np.sin(f)
            ylist.insert(0,y)
            #saves to a file
            print(tlist[0], "  ", flist[0], "  ", rlist[0], "  ", xlist[0], "  ", ylist[0], file = open("ephem.txt", "a"))

        #creates table
        plt.figure(1)
        plt.subplot(211)
        plt.plot(tlist,rlist)
        plt.ylabel('radius')
        plt.xlabel('time')
        plt.subplot(212)
        plt.plot(tlist,flist)
        #completes the loop
        tlist.insert(0,tlist[loopcount-1])
        rlist.insert(0,rlist[loopcount-1])
        flist.insert(0,flist[loopcount-1])
        xlist.insert(0,xlist[loopcount-1])
        ylist.insert(0,ylist[loopcount-1])
        plt.figure(2)
        plt.plot(xlist,ylist)
    
        plt.figure(3)
        theta = np.linspace(0,2*np.pi, 360)
        r = (Semimajoraxis*(1-eccentricity**2))/(1+eccentricity*np.cos(theta))
        plt.polar(theta, r)
    
        plt.show()
        plt.show()

    if __name__== "__main__":
  
        main()
        
        answer = str(input('Run again? (y/n): '))
        if answer == 'y':
            continue
        else:
            print ('Goodbye')
            break
                    
#        if answer in ('y', 'n'):
           # break
            #print ('Invalid input.')





