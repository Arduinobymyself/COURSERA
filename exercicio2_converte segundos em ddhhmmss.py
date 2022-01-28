
"""
Converte segundos em
dias, horas, minutos e segundos
"""

segundos = int(input('Entre com o número de segundos que deseja converter: '))
dias = segundos // 86400
segundos_restantes = segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60


#print('{} dias {} horas {} minutos {} segundos'.format(dias,horas,minutos,segundos_final))
print(dias, 'dias,',horas, 'horas,',minutos,'minutos e',segundos_final,'segundos.')
