from PWM_algoritme import leftmotorspeed
from PWM_algoritme import rightmotorspeed
from PWM_algoritme import forward
from PWM_algoritme import backwards
from PWM_algoritme import stopMotor
from PWM_algoritme import motorcleanup
from PWM_algoritme import motorinitialisatie
from runfile_Lijnsensor_pycharm import lijndataTabel





forward(30)
data = lijndataTabel()
CALIBRATEDMINIMUM = data
CALIBRATEDMAXIMUM = data
for k in range(100):
    data = lijndataTabel()
    for i in range(len(data)):
        if data[i] < CALIBRATEDMINIMUM[i] and data[i] != 0:
            CALIBRATEDMINIMUM[i] = data[i]
        if data[i] > CALIBRATEDMAXIMUM:
            CALIBRATEDMAXIMUM[i] = data[i]
    time.sleep(0.05)

stopMotor()
print("minimum:")
print(CALIBRATEDMINIMUM)
print()
print("maximum:")
print(CALIBRATEDMAXIMUM)


