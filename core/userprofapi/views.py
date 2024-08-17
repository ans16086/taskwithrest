
#from rest_framework import generics
from userprof.models import *
from .serializers import PostaddressSerializer
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
'''''
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def userprofotest(request):
   if request.method == 'GET':
       TESTO ={
      'A':'a',
      'B':['b','e'],
      'C':'c',
       }
       return Response(TESTO)

   elif request.method == 'POST':
       data=request.data
       print('in post')
       print(data)

       return Response(data)
   
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def userprofo(request):
       if request.method == 'GET':
            data = userprofilee.objects.all()
            #data1=deletebutton.objects.all()
            serilizers=PostaddressSerializer(data,many=True)
            return Response(serilizers.data)
       elif request.method == 'POST':
            data = request.data
            serilizers=PostaddressSerializer(data=data)
            if serilizers.is_valid():
                 serilizers.save()
                 return Response(serilizers.data) 
            return Response(serilizers.errors)   
