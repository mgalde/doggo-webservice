from rest_framework import serializers
from api.models import Dog, Breed, BREEDDEFINE, BREEDRATE

class BreedSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	breedname = serializers.CharField(required=True, allow_blank=False, max_length=100)
	breedsize = serializers.ChoiceField(choices=BREEDDEFINE)
	friendliness = serializers.ChoiceField(choices=BREEDRATE)
	trainability = serializers.ChoiceField(choices=BREEDRATE)
	sheddingamount = serializers.ChoiceField(choices=BREEDRATE)
	exerciseneeds = serializers.ChoiceField(choices=BREEDRATE)

	def create(self, validated_data):
		return Breed.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.breedname = validated_data.get('breedname', instance.breedname)
		instance.breedsize = validated_data.get('breedsize', instance.breedsize)
		instance.friendliness = validated_data.get('friendliness', instance.friendliness)
		instance.trainability = validated_data.get('trainability', instance.trainability)
		instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
		instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
		instance.save()
		return instance

class DogSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	dogname = serializers.CharField(required=True, allow_blank=False, max_length=100)
	dogage = serializers.IntegerField(required=False)
	dogbreed = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Breed.objects.all())
	doggender = serializers.CharField(required=False, max_length=50)
	dogcolor = serializers.CharField(required=False, max_length=50)
	dogfood = serializers.CharField(required=False, max_length=100)
	dogtoy = serializers.CharField(required=False, max_length=100)

	def create(self, validated_data):
		return Dog.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.dogname = validated_data.get('dogname', instance.dogname)
		instance.dogage = validated_data.get('dogage', instance.dogage)
		instance.dogbreed = validated_data.get('dogbreed', instance.dogbreed)
		instance.doggender = validated_data.get('doggender', instance.doggender)
		instance.dogcolor = validated_data.get('dogcolor', instance.dogcolor)
		instance.dogfood = validated_data.get('dogfood', instance.dogfood)
		instance.dogtoy = validated_data.get('dogtoy', instance.dogtoy)
		instance.save()
		return instance
