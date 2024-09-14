from .serializer import  ChampionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Champion


#Json Response View
class ChampionsView(APIView):


    def get(self, request):
            try:
                champions = Champion.objects.all()
                serializer = ChampionSerializer(champions,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'error':'Error al intentar serealizar los datos.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def post(self, request):
        if not request.data:
             return Response({'Error':'Ingrese un nombre valido de campeon'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if request is not None:
                 champion_name = request.data.get('nombre')
                 champion = Champion.objects.get(nombre=champion_name.capitalize())
                 serializer = ChampionSerializer(champion)
                 return Response(serializer.data, status=status.HTTP_200_OK)
            
    
        
        except Champion.DoesNotExist:
            return Response({"Error": f"Campeon '{champion_name}' no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        



#Query View
class ChampionDetailView(APIView):
     
     def get(self, request, champion_name):
              
              champion = Champion.objects.filter(nombre__iexact=champion_name.capitalize()).first()
              if champion:
                   serializer = ChampionSerializer(champion)
                   return Response(serializer.data, status=status.HTTP_200_OK)
              else:
                   return Response({"Error":"Campeon Inexistente"}, status=status.HTTP_404_NOT_FOUND)




