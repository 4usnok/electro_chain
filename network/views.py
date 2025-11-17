from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from network.models import Network
from network.serializers import MyTokenObtainPairSerializer, NetworkSerializer


class NetworkList(generics.ListAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get("country_cont")
        if country:
            # Фильтруем по стране
            queryset = queryset.filter(contacts_fact__country_cont=country)
        return queryset.distinct()


class NetworkDetail(generics.RetrieveAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated]


class NetworkCreate(generics.CreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated]


class NetworkUpdate(generics.UpdateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated]


class NetworkDelete(generics.DestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
