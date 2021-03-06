from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from auth.serializers import UserSerializer

from rest_framework import authentication, exceptions

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class PostView(ListAPIView):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated)


class ExampleAuthentication(authentication.BasicAuthentication):
	def authenticate(self, request):
		username = request.META.get('X_USERNAME')
		if not username:
			return None
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise exceptions.AuthenticationFailed('No such user')

		return (user, None)


from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 

class CustomAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})

		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'email': user.email
			})




# class ExampleView(APIView):
# 	authentication_classes = (SessionAuthetication, BasicAuthentication)
# 	permission_classes = (IsAuthenticated,)

# 	def get(self, request, format=None):
# 		content = {
# 			'user': unicode(request.user),
# 			'auth': unicode(request.auth),
# 		}
# 		return Response(content)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    permission_classes = (AllowAny,)

    def post(self, request, format='json'):	
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.is_valid())
        print(serializer)
















