from django.utils.html import strip_tags
from rest_framework import serializers, status

from ..models import Job, JobHeader


class ChoiceField(serializers.ChoiceField):
    """
    This is custom choice field. It must save in db shorter choice fields, but accept and return longer
    ORIGIN: https://stackoverflow.com/questions/28945327/django-rest-framework-with-choicefield
    """

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class JobHeaderSerializer(serializers.ModelSerializer):
    plain_title_text = serializers.SerializerMethodField()

    class Meta:
        model = JobHeader
        fields = ["id", "rich_title_text", "rich_subtitle_text", "plain_title_text"]

    def get_plain_title_text(self, obj):
        return strip_tags(obj.rich_title_text)


class JobSerializer(serializers.ModelSerializer):
    type = ChoiceField(choices=Job.JobTypeChoices.choices)
    header = JobHeaderSerializer(many=False, required=True)

    class Meta:
        model = Job
        fields = ["id", "name", "type", "header"]

    def create(self, validated_data: dict):
        header_data = validated_data.pop("header", None)
        if header_data is None:
            raise serializers.ValidationError(
                detail={"detail": "Job header data was not provided"},
                code=status.HTTP_400_BAD_REQUEST
            )
        job = Job.objects.create(
            name=validated_data["name"],
            type=validated_data["type"]
        )

        JobHeader.objects.create(**header_data, job=job)
        return job
