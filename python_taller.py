# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:33:17 2021

@author: oscar perez
"""
#cardiaco
edad=55;
numero= (200 - edad)/10;
print ((numero));

#masa
presion=20;
volumen=10;
temperatura=3;
masa= (presion * volumen) / (0.37 * (temperatura + 460));

print (masa);

#porcentaje
persona1=10000;
persona2=20000;
persona3=30000;
suma= persona1+persona2+persona3;
print ('la invercion total es', suma);

porp1= (persona1/suma)*100;
print ('porcentaje de la primera persona es', porp1, "%");

porp2= (persona2/suma)*100;
print ('porcentaje de la segunda persona es', porp2, '%' );

porp3= (persona3/suma)*100;
print ('porcentaje de la tercera persona es de', porp3, '%');
