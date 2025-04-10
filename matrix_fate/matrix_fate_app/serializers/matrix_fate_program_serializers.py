from rest_framework import serializers

from matrix_fate_app.models import MatrixFateProgram

class MatrixFateProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatrixFateProgram
        fields = '__all__'


class MatrixFateInputSerializer(serializers.Serializer):
    day = serializers.IntegerField(min_value=1, max_value=31)
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=1000, max_value=9999)
    category = serializers.ChoiceField(
        choices=["matrix_fate", "finance", "compatibility", "child"],
        default="matrix_fate",
        required=False
    )


class MatrixFateOutputSerializer(serializers.Serializer):

    category = serializers.CharField()
    a = serializers.IntegerField(required=False)
    a1 = serializers.IntegerField(required=False)
    a2 = serializers.IntegerField(required=False)

    b = serializers.IntegerField(required=False)
    b1 = serializers.IntegerField(required=False)
    b2 = serializers.IntegerField(required=False)

    c = serializers.IntegerField(required=False)
    c1 = serializers.IntegerField(required=False)
    c2 = serializers.IntegerField(required=False)

    d = serializers.IntegerField(required=False)
    d1 = serializers.IntegerField(required=False)
    d2 = serializers.IntegerField(required=False)

    e = serializers.IntegerField(required=False)
    e1 = serializers.IntegerField(required=False)
    e2 = serializers.IntegerField(required=False)

    f = serializers.IntegerField(required=False)
    f1 = serializers.IntegerField(required=False)
    f2 = serializers.IntegerField(required=False)

    g = serializers.IntegerField(required=False)
    g1 = serializers.IntegerField(required=False)
    g2 = serializers.IntegerField(required=False)

    h = serializers.IntegerField(required=False)
    h1 = serializers.IntegerField(required=False)
    h2 = serializers.IntegerField(required=False)

    i = serializers.IntegerField(required=False)
    i1 = serializers.IntegerField(required=False)
    i2 = serializers.IntegerField(required=False)

    j = serializers.IntegerField(required=False)
    k = serializers.IntegerField(required=False)
    l = serializers.IntegerField(required=False)
    
    m = serializers.IntegerField(required=False)
    n = serializers.IntegerField(required=False)

    r = serializers.IntegerField(required=False)
    s = serializers.IntegerField(required=False)
    y = serializers.IntegerField(required=False)

    t = serializers.IntegerField(required=False)
    u = serializers.IntegerField(required=False)
    v = serializers.IntegerField(required=False)
    
    w = serializers.IntegerField(required=False)
    x = serializers.IntegerField(required=False)

    o = serializers.IntegerField(required=False)
    o1 = serializers.IntegerField(required=False)
    o2 = serializers.IntegerField(required=False)
    o3 = serializers.IntegerField(required=False)
    o4 = serializers.IntegerField(required=False)
    o5 = serializers.IntegerField(required=False)
    o6 = serializers.IntegerField(required=False)
    o7 = serializers.IntegerField(required=False)

    p = serializers.IntegerField(required=False)
    p1 = serializers.IntegerField(required=False)
    p2 = serializers.IntegerField(required=False)
    p3 = serializers.IntegerField(required=False)
    p4 = serializers.IntegerField(required=False)
    p5 = serializers.IntegerField(required=False)
    p6 = serializers.IntegerField(required=False)
    p7 = serializers.IntegerField(required=False)

    q = serializers.IntegerField(required=False)
    q1 = serializers.IntegerField(required=False)
    q2 = serializers.IntegerField(required=False)
    q3 = serializers.IntegerField(required=False)
    q4 = serializers.IntegerField(required=False)
    q5 = serializers.IntegerField(required=False)
    q6 = serializers.IntegerField(required=False)
    q7 = serializers.IntegerField(required=False)

#a
    a5 = serializers.IntegerField(required=False)
    a2_3 = serializers.IntegerField(required=False)
    a3_4 = serializers.IntegerField(required=False)
    a1_2 = serializers.IntegerField(required=False)
    a7_8 = serializers.IntegerField(required=False)
    a8_9 = serializers.IntegerField(required=False)
    a6_7 = serializers.IntegerField(required=False)
#
    f15 = serializers.IntegerField(required=False)
    f12_13 = serializers.IntegerField(required=False)
    f13_14 = serializers.IntegerField(required=False)
    f11_12 = serializers.IntegerField(required=False)
    f17_18 = serializers.IntegerField(required=False)
    f18_19 = serializers.IntegerField(required=False)
    f16_17 = serializers.IntegerField(required=False)
#
    b25 = serializers.IntegerField(required=False)
    b22_23 = serializers.IntegerField(required=False)
    b23_24 = serializers.IntegerField(required=False)
    b21_22 = serializers.IntegerField(required=False)
    b27_28 = serializers.IntegerField(required=False)
    b28_29 = serializers.IntegerField(required=False)
    b26_27 = serializers.IntegerField(required=False)
#
    g35 = serializers.IntegerField(required=False)
    g32_33 = serializers.IntegerField(required=False)
    g33_34 = serializers.IntegerField(required=False)
    g31_32 = serializers.IntegerField(required=False)
    g37_38 = serializers.IntegerField(required=False)
    g38_39 = serializers.IntegerField(required=False)
    g36_37 = serializers.IntegerField(required=False)
#
    c41_42 = serializers.IntegerField(required=False)
    c42_43 = serializers.IntegerField(required=False)
    c43_44 = serializers.IntegerField(required=False)
    c45 = serializers.IntegerField(required=False)
    c46_47 = serializers.IntegerField(required=False)
    c47_48 = serializers.IntegerField(required=False)
    c48_49 = serializers.IntegerField(required=False)
#
    h51_52 = serializers.IntegerField(required=False)
    h52_53 = serializers.IntegerField(required=False)
    h53_54 = serializers.IntegerField(required=False)
    h55 = serializers.IntegerField(required=False)
    h56_57 = serializers.IntegerField(required=False)
    h57_58 = serializers.IntegerField(required=False)
    h58_59 = serializers.IntegerField(required=False)
#
    d61_62 = serializers.IntegerField(required=False)
    d62_63 = serializers.IntegerField(required=False)
    d63_64 = serializers.IntegerField(required=False)
    d65 = serializers.IntegerField(required=False)
    d66_67 = serializers.IntegerField(required=False)
    d67_68 = serializers.IntegerField(required=False)
    d68_69 = serializers.IntegerField(required=False)
#
    i71_72 = serializers.IntegerField(required=False)
    i72_73 = serializers.IntegerField(required=False)
    i73_74 = serializers.IntegerField(required=False)
    i75 = serializers.IntegerField(required=False)
    i76_77 = serializers.IntegerField(required=False)
    i77_78 = serializers.IntegerField(required=False)
    i78_79 = serializers.IntegerField(required=False)
    
