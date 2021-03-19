

from Lijnsensor_pycharm import lijndataTabel


CALIBRATEDMINIMUM =  #maximumtijdswaardetabel
CALIBRATEDMAXIMUM  = 1 #minimumtijdswaardetabel

def herschaalwaarde(lijndataTabel, minimum, maximum): #noteert iedere waarde als een getal tussen 0 en 1000 ("read calibrate")
    #hulpfunctie voor readpositie
    herschaaltabel = []
    for k in range(len(lijndataTabel)):
        herschaaldewaarde = (lijndataTabel[i] - minimum[i])/(maximum[i]-minimum[i])*1000
        if herschaaldewaarde < minimum[i]:
            herschaaldewaarde = minimum[i]
        if herschaaldewaarde > maximum[i]:
            herschaaldewaarde = maximum[i]
        herschaaltabel.append(herschaaldewaarde)
    return herschaaltabel

def readpositie(lijndatatabel, minimum = CALIBRATEDMINIMUM, maximum = CALIBRATEDMAXIMUM):
    #gebruikte formule: (0*value0 + 1000*value1+ 2000*value2) /(value0 + value1 + value2)
    #geeft een waarde voor de positie
    herschaaltabel = herschaalwaarde(lijndatatabel, minimum, maximum) #geeft tabel met de gekalibreerde waardes: tussen 0 en 1000
    avg = 0
    som = 0
    for i in range(len(herschaaltabel)):
        if herschaaltabel[i] > 50: #ruis wegwerken
            avg += (i*1000)*herschaaltabel[i]
            som += herschaaltabel[i]

    return avg/som

#while True
def volglijn():
