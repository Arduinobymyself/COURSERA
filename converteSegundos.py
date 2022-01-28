segundos = int(input('Entre com o número de segundos que deseja converter: '))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60

print('{} horas {} minutos {} segundos'.format(horas,minutos,segundos_final))
