from rest_framework import serializers

from goods.models import SpecificationOption, SPUSpecification


class SpecsOptionsSerializer(serializers.ModelSerializer):
    spec = serializers.StringRelatedField()
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = ['id', 'value', 'spec', 'spec_id']


class OptionSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPUSpecification
        fields = ['id', 'name']
