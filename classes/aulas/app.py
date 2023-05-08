from evento import Events
from evento_online import EventoOnline

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")

print(ev_online.to_json())
print(ev2_online.to_json())

ev = Events("Aula de JavaScript", "Manaus")
ev.imprime_informacoes()
