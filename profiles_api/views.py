from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializer, models


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """return get """

        an_apiview = [
            'Uses HTTP method get post del put and push ',
            "lalalla",
            'blalala',
        ]

        return Response({'message': 'Hello, I"m API', 'an_apiview': an_apiview})

    def post(self, request):
        """post method """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handles the object"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """partial update of fields """
        return Response({'message': 'Patch'})

    def delete(self, request, pk=None):
        """partial update of fields """
        return Response({'message': 'delete '})


class HelloViewSet(viewsets.ViewSet):
    """testing view set"""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses HTTP method get post del put and push ',
            "lalalla",
            'blalala',
            'sam',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create hello msg """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle get user id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Update obj"""
        return Response({'http_method': 'put'})

    def partial_update(self, request, pk=None):
        """update partialy """
        return Response({'http_method': 'patch'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating model view set"""

    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
