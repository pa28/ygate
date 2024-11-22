#!/usr/bin/python  -u 

from gpiozero import CPUTemperature
import psutil

cpu = CPUTemperature()
print(round(cpu.temperature, 1))
load = psutil.getloadavg()[0] / psutil.cpu_count() * 100
print('CPU Load: ', load, round(load,0))
