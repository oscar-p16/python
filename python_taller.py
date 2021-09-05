# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:33:17 2021

@author: oscar perez
"""
#cardiaco
edad=55;
numero= (200 - edad)/10;
print ((numero));
print ("//////////////////////////////////////");
#masa
presion=20;
volumen=10;
temperatura=3;
masa= (presion * volumen) / (0.37 * (temperatura + 460));

print (masa);
print ("//////////////////////////////////////");
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

#banco
print ("//////////////////////////////////////");
numeromeses=10;
saldoinicial=50000;
totaldinero= (saldoinicial*0.15)*numeromeses;
print ("el saldo total es",totaldinero);

print ("//////////////////////////////////////");
#empleados
salario= 1000000;
descuento1= salario*0.01;
print ("descuento por ley de politica publica", descuento1);
descuento2= salario*0.04;
print("descuento por seguro social", descuento2);
descuento3= salario*0.005;
print("descuento por seguro forzoso", descuento3);
descuento4= salario*0.05;
print("descuento por caja de ahorro", descuento4);

totalp= ((((salario-descuento1)-descuento2)-descuento3)-descuento4);
print ("el total del salario del empleado es", totalp);

print ("//////////////////////////////////////");
#periodico
palabra=50;
centimetro=20;
color=2;
cpalabra=20000;
ccentimetro=15000;
ccolor=25000;
totalperiodico= (palabra * cpalabra)+(centimetro*ccentimetro)+(color* ccolor);
print ("el total del anuncio es", "$", totalperiodico);

print ("//////////////////////////////////////");

#empresa
años = int(input("digite años del empleado: "))
if años>=1 :
    bonoinicial=100000;
    bonosegundario= ((años-1)*120000)+bonoinicial;
    print('el bono final es', bonosegundario);

print ("//////////////////////////////////////");

#univercidad
horas = int(input("numero de horas: "));
horasp= 20000;
horast= horas*horasp
descuento= horast*0.05;
totalpagar= horast-descuento;
print('total a pagar','$', totalpagar)
print ('descuento total', descuento);

print ("//////////////////////////////////////");

#comunicaciones

monini=int(input("ingrese monto inicial: "));
montifin= int(input("ingrese monto final: "));
costofinal=(monini-montifin)*0.20
print("costo total es", "$", costofinal);







