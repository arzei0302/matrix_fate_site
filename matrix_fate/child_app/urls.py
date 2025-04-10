from django.urls import path

from child_app.service.matrix_child_calc import calculate_child_matrix_view
from child_app.views.child_greatest_talent_views import (
    ChildCategoryWithBusinessCardAPIView,
)
from child_app.views.child_parent_karma_views import (
    ChildCategoryWithParentKarmaAPIView,
)
from child_app.views.child_personal_qualities_views import (
    ChildCategoryWithPersonalQualitiesAPIView,
)
from child_app.views.child_point_of_comfort_views import (
    ChildCategoryWithPointOfComfortAPIView,
)
from child_app.views.child_self_realization_views import (
    ChildCategoryWithSelfRealizationAPIView,
)
from child_app.views.tasks_child_destiny_views import (
    ChildCategoryWithDestinyAPIView,
)
from child_app.views.tasks_from_past_lives_views import (
    ChildCategoryWithPastLivesTasksAPIView,
)


urlpatterns = [
    path(
        "child_business_card/<str:category_id_or_title>/",
        ChildCategoryWithBusinessCardAPIView.as_view(),
        name="child_business_card",
    ),
    path(
        "child_personal_qualities/<str:category_id_or_title>/",
        ChildCategoryWithPersonalQualitiesAPIView.as_view(),
        name="child_personal_qualities",
    ),
    path(
        "child_self_realization/<str:category_id_or_title>/",
        ChildCategoryWithSelfRealizationAPIView.as_view(),
        name="child_self_realization",
    ),
    path(
        "child_point_of_comfort/<str:category_id_or_title>/",
        ChildCategoryWithPointOfComfortAPIView.as_view(),
        name="child_point_of_comfort",
    ),
    path(
        "tasks_from_past_lives/<str:category_id_or_title>/",
        ChildCategoryWithPastLivesTasksAPIView.as_view(),
        name="tasks_from_past_lives",
    ),
    path(
        "child_destiny/<str:category_id_or_title>/",
        ChildCategoryWithDestinyAPIView.as_view(),
        name="child_destiny",
    ),
    path(
        "child_parent_karma/<str:category_id_or_title>/",
        ChildCategoryWithParentKarmaAPIView.as_view(),
        name="child_parent_karma",
    ),

    path(
        "calculate-child-matrix/", calculate_child_matrix_view, 
        name="calculate-child-matrix"),
]
