from rest_framework import serializers

class MatrixCompability2InputSerializer(serializers.Serializer):
    day = serializers.IntegerField(min_value=1, max_value=31)
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=1000, max_value=9999)

    day2 = serializers.IntegerField(min_value=1, max_value=31)
    month2 = serializers.IntegerField(min_value=1, max_value=12)
    year2 = serializers.IntegerField(min_value=1000, max_value=9999)


class MatrixCompability2OutputSerializer(serializers.Serializer):
    category = serializers.CharField() 
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    c = serializers.IntegerField()
    c2 = serializers.IntegerField()
    d = serializers.IntegerField()
    d1 = serializers.IntegerField()
    d2 = serializers.IntegerField()
    e = serializers.IntegerField()
    f = serializers.IntegerField()
    g = serializers.IntegerField()
    h = serializers.IntegerField()
    i = serializers.IntegerField()
    j = serializers.IntegerField()
    k = serializers.IntegerField()
    l = serializers.IntegerField()
    r = serializers.IntegerField()
    s = serializers.IntegerField()
    y = serializers.IntegerField()
    t = serializers.IntegerField()
    u = serializers.IntegerField()
    v = serializers.IntegerField()
    w = serializers.IntegerField()

    
