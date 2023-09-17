#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Las 4 primeras lineas con para las palabras con acentos

texto = "practicas python"
texto2 = "PRACTICAS PYTHON"
texto3 = "PrAcTiCas PyThOn"

texto = texto.title()

print(texto) #pone en mayusculas la primera letra de cada palabra
print(texto.title())

print(texto.upper()) #pone en mayusculas todas las letras

print(texto2.lower()) #pone en minusculas todas las letras

print(texto3.title()) #formatea todo esl texto y hace su funcion
