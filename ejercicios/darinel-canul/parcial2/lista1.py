"""""
 trabajas en a organizacion de un evento de premios tienes una lista de celebridades que entraran por la alfombra y ojo. El orden es vital
1.crea una lista llamada invitados con lo nombres 
 "Robert Doeny jr", "Emma Estone"  "Cilian Murphy"

2.Llegada de ultimo minuto. Agrega a "Zendaya" al final de la lista
3.invitado vip. "Steven Sprelber" acaba de llegar de llegar u debe ir al principio de la lista 
4.cancelacion. "Emma Stone" avisa que no podra estar 
5. Seguridad. El ultimo de la lista se porto mal y debe ser retirado
6. Imprime la lista final y cuantos invitados quedan en total.
"""""
#punto no.1
invitados= ("Robert Downy jr","Emma Stone","Cilian Murphy")
#punto no.2
invitados.append("Zendaya")
#punto no.3
invitados.insert(0,"Sreven Sprelber")
#punto no.4
invitados.remove("Emma Stone")
#punto no.5
invitados.pop(3)
#punto no.6
print(invitados, "No. total invitados:", len (invitados))