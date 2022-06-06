from rest_framework import serializers
from .models import Sede,Dependencia,sedeDependencia

class sedeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Sede
		fields='__all__'

class dependenciaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Dependencia
		fields='__all__'

class sedeDepSerializer(serializers.ModelSerializer):
	class Meta:
		model=sedeDependencia
		fields='__all__'
