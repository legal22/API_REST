from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer


class HelloApiView(APIView):
    """API View de Prueba"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        #Retornar lista de caracteristicas del APIView
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        #crea un mensaje con nuestro nombre
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        #maneja actualizar un objeto
        return Response({'method': 'PUT'})
    
    def patch(self, request, ph=None):
        #maneja actualizacion parcial de un objeto
        return Response({'method': 'PATCH'})

    def delete(self, request, ph=None):
        #Borrar un objeto
        return Response({'method': 'DELETE'})