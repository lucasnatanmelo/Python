from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer, PrestadorSerializer
from agenda.utils import get_horarios_disponiveis

"""
- Qualquer cliente (autenticado ou não) seja capaz de criar um agendamento.
- Apenas o prestador de serviço pode vizualizar todos os agendamentos em sua agenda.
- Apendas o prestador de serviço pode manipular os seus agendamentos
"""

class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        username = request.query_params.get("username", None)
        if request.user.username == username:
            return True
        return False

class IsPrestador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False

# FIFTY METHOD - Using generics - using username as key
class AgendamentoList(generics.ListCreateAPIView):  # /api/agendamentos/?username=lucas.melo
    serializer_class = AgendamentoSerializer
    # implements authentication -> only the related user 
    permission_classes = [IsOwnerOrCreateOnly]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Agendamento.objects.filter(prestador__username = username) # fix it to receive a str, not a integer
        return queryset 

# FOURTH METHOD - Using generics
class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView): # /api/agendamentos/<pk>/

    permission_classes = [IsPrestador]
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class PrestadorList(generics.ListAPIView):  # /api/agendamentos/prestadores

    # Implements super user authentication here

    serializer_class = PrestadorSerializer
    queryset = User.objects.all()

# Create your views here.

# FIRST METHOD:
# @api_view(http_method_names=["GET", "POST"])
# def agendamentos_list(request):

#     if request.method == "GET":
#         qs = Agendamento.objects.all()
#         serializer = AgendamentoSerializer(qs, many=True)
#         # safe = False -> To retunr a list of Agendamento
#         return JsonResponse(serializer.data, safe=False)
#     if request.method == "POST":
#         data = request.data
#         serializer = AgendamentoSerializer(data=data)
#         # verify if all values are valid with serializers
#         if serializer.is_valid():

#             # save() -> save is a pre-defined method designed by django framework 
#             serializer.save()
#             return JsonResponse(serializer.data ,status=201)
        
#         return JsonResponse(serializer.errors, status=400)

# SECOND METHOD:
# class AgendamentoList(APIView):
#     def get(self, request):
#         qs = Agendamento.objects.all()
#         serializer = AgendamentoSerializer(qs, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request):
#         data = request.data
#         serializer = AgendamentoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# THIRD METHOD - Using Mixins
# class AgendamentoList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):  
#     queryset = Agendamento.objects.all()
#     serializer_class = AgendamentoSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# FOURTH METHOD - Using generics
# class AgendamentoList(generics.ListCreateAPIView):  # /api/agendamentos/
#     queryset = Agendamento.objects.all()
#     serializer_class = AgendamentoSerializer

# ----------------------------------------------------------------------------------------

# FIRST METHOD:
# @api_view(http_method_names=["GET", "PATCH", "DELETE"])
# def agendamento_detail(request, id):

#     # get_object_or_404() -> this method will search the Agendamento instance by your id
#     obj = get_object_or_404(Agendamento, id=id)

#     if request.method == "GET":
#         # serialize the object attributes to send as JSON
#         serializer = AgendamentoSerializer(obj)
#         return JsonResponse(serializer.data)
    
#     if request.method == "PATCH":
#         data = request.data
#         # partial = True -> The data does not need to have all the arguments to be filled
#         serializer = AgendamentoSerializer(obj, data=data, partial=True)
#         # verify if all values are valid with serializers
#         if serializer.is_valid():
#             serializer.save()
#             # validated_data -> will return only the changed data
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)
    
#     if request.method == "DELETE":
#         obj.delete()
#         return Response(status=204)

# SECOND METHOD:
# class AgendamentoDetail(APIView):
    
#     def get(self, request, id):
#         # get_object_or_404() -> this method will search the Agendamento instance by your id
#         obj = get_object_or_404(Agendamento, id=id)
        
#         # serialize the object attributes to send as JSON
#         serializer = AgendamentoSerializer(obj)
#         return JsonResponse(serializer.data)

#     def patch(self, request, id):
#         # get_object_or_404() -> this method will search the Agendamento instance by your id
#         obj = get_object_or_404(Agendamento, id=id)

#         data = request.data
#         # partial = True -> The data does not need to have all the arguments to be filled
#         serializer = AgendamentoSerializer(obj, data=data, partial=True)
#         # verify if all values are valid with serializers
#         if serializer.is_valid():
#             serializer.save()
#             # validated_data -> will return only the changed data
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)
    
#     def delete(self, request, id):
#         # get_object_or_404() -> this method will search the Agendamento instance by your id
#         obj = get_object_or_404(Agendamento, id=id)

#         obj.delete()
#         return Response(status=204)

# THIRD METHOD:
# class AgendamentoDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Agendamento.objects.all()
#     serializer_class = AgendamentoSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
        
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Finish it later

@api_view(http_method_names=["GET"])
def get_horarios(request):
    data = request.query_params.get("data")
    if not data:
        data = datetime.now().date()
    else:
        data = datetime.fromisoformat(data).date()

    horarios_disponiveis = sorted(list(get_horarios_disponiveis(data)))
    return JsonResponse(horarios_disponiveis, safe=False)
