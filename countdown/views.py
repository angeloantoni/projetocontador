from django.shortcuts import render
import datetime

def countdown_view(request):
    data_inicial = datetime.datetime(2024, 12, 16, 0, 0, 0)
    data_final = datetime.datetime(2025, 2, 16, 23, 59, 59)
    hoje = datetime.datetime.now()
    
    if hoje < data_inicial:
        tempo_restante = data_inicial - hoje 
        context = {
            "mensagem": "Clara viaja em: ",
            "dias": tempo_restante.days, 
            "horas": tempo_restante.seconds // 3600,
            "minutos": (tempo_restante.seconds // 60) % 60,
            "segundos": tempo_restante.seconds % 60,
            "data_inicial": data_inicial.isoformat(),
            "data_final": data_final.isoformat(),
            "hoje": hoje.isoformat()
        }
    elif data_inicial <= hoje <= data_final:
        tempo_restante = data_final - hoje
        context = {
            "mensagem": "Volta em: ",
            "dias": tempo_restante.days, 
            "horas": tempo_restante.seconds // 3600,
            "minutos": (tempo_restante.seconds // 60) % 60,
            "segundos": tempo_restante.seconds % 60,
            "data_inicial": data_inicial.isoformat(),
            "data_final": data_final.isoformat(),
            "hoje": hoje.isoformat()
        }
    else: 
        context = {
            "mensagem": "Voltou :)",
            "dias": 0, 
            "horas": 0,
            "minutos": 0,
            "segundos": 0,
            "data_inicial": data_inicial.isoformat(),
            "data_final": data_final.isoformat(),
            "hoje": hoje.isoformat()
        }
    return render(request, 'countdown/index.html', context)
