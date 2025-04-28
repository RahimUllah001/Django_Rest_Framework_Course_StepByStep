from .models import Singer,Song

from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        # fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name = 'song-detail')
    sungby = SongSerializer(many=True,read_only=True)
    class Meta:
        model = Singer
        # fields = ['id','name','gender','song'] #if here i use 'song' field without defining the song aove the meta class then it will show only th eid of the song and it i use the above definition of song abve merta then it will show its  all detail 
        fields = ['id','name','gender','sungby'] # nested serializer Singer info and inside it thee will alos his all songs information