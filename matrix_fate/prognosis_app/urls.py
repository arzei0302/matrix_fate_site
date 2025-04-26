from django.urls import path

from matrix_fate.prognosis_app.age_views import BreakdownByYearListView
# from .views import PrognosisByOrderAPIView
from .views import PrognosisByBirthDateAPIView


urlpatterns = [
    # path("prognosis/", PrognosisByOrderAPIView.as_view(), name="prognosis-by-order"),
    path("prognosis/", PrognosisByBirthDateAPIView.as_view(), name="prognosis-by-order"),

    path('api/breakdown/', BreakdownByYearListView.as_view(), name='breakdown-by-year'),

]
