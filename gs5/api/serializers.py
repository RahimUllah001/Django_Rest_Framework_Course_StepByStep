from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # Validator
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']  # Use this to make fields read-only
        # extra_kwargs = {'name': {'read_only': True}}  # Use this to make fields read-only
        # extra_kwargs = {'name': {'required': False}}  # Use this to make fields optional
        # extra_kwargs = {'name': {'validators': []}}  # Use this to remove validators
        # extra_kwargs = {'name': {'error_messages': {'required': 'Please enter your name'}}}  # Use this to customize error messages
        # extra_kwargs = {'name': {'default': 'Anonymous'}}  # Use this to set default values
        # extra_kwargs = {'name': {'help_text': 'Your name'}}  # Use this to add help text
        # extra_kwargs = {'name': {'label': 'Full Name'}}  # Use this to change field labels
        # extra_kwargs = {'name': {'style': {'template': 'textinput.html'}}}  # Use this to add custom styles
        # extra_kwargs = {'name': {'write_only': True}}  # Use this to make fields write-only
        # extra_kwargs = {'name': {'allow_null': True}}  # Use this to allow null values
        # extra_kwargs = {'name': {'allow_blank': True}}  # Use this to allow blank values
        # extra_kwargs = {'name': {'min_length': 10}}  # Use this to set minimum length
        # extra_kwargs = {'name': {'max_length': 100}}  # Use this to set maximum length
        # extra_kwargs = {'name': {'strip': False}}  # Use this to disable stripping
        # extra_kwargs = {'name': {'trim_whitespace': False}}  # Use this to disable trimming
        # extra_kwargs = {'name': {'truncate_whitespace': False}}  # Use this to disable truncating
        # extra_kwargs = {'name': {'empty': False}}  # Use this to disallow empty values
        # extra_kwargs = {'name': {'empty': True}}  # Use this to allow empty values
        # extra_kwargs = {'name': {'allow_empty_file': False}}  # Use this to disallow empty files
        # extra_kwargs = {'name': {'allow_empty_file': True}}  # Use this to allow empty files
        # extra_kwargs = {'name': {'binary': False}}  # Use this to disallow binary files
        # extra_kwargs = {'name': {'binary': True}}  # Use this to allow binary files
        # extra_kwargs = {'name': {'coerce_to_string': False}}  # Use this to disable coercion


    # Field Level validators
    def validate_roll(self, value):
        if value >= 500:
            raise serializers.ValidationError('Rollnumber should not be greater than 500')
        return value

    # Object Level validators we ue this method to validate multiple fields at a time
    def validate(self, data):
        roll = data.get('roll')
        ct = data.get('city')
        if ct.lower() == 'wazir' and roll < 300:    
            raise serializers.ValidationError('roll no should be greater than 300')
        return data