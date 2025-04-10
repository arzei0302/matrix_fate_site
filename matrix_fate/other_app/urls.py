from django.urls import path
from other_app.views.access_views import AccessMatrixDetailView, AccessMatrixListView
# from other_app.views.additional_views import RandomTarotReadingView, RandomArcanaCluesView
from other_app.views.footer_views import MessageSupportDetailView, PrivacyPolicyDetailView, PublicOfferAgreementDetailView
from other_app.views.social_link_vews import SocialLinkDetailView
# from other_app.views.fin_and_anti_code_views import FinancialAndAntiCodeByBirthDateView
# from other_app.views.yes_no_maybe_answer import YesNoMaybeAnswerView


urlpatterns = [
    path('tariffs/', AccessMatrixListView.as_view(), name='access_matrix_list'),
    path('tariffs/<int:id>/', AccessMatrixDetailView.as_view(), name='access_matrix_detail'),

    path('message-support/<int:pk>/', MessageSupportDetailView.as_view(), name='message-support-detail'),
    path('privacy-policy/<int:pk>/', PrivacyPolicyDetailView.as_view(), name='privacy-policy-detail'),
    path('public-offer-agreement/<int:pk>/', PublicOfferAgreementDetailView.as_view(), name='public-offer-agreement-detail'),
    path('social-links/<int:pk>/', SocialLinkDetailView.as_view(), name='social-link-detail'),


    # path('random-tarot-reading/', RandomTarotReadingView.as_view(), name='random-tarot-reading'),
    # path('arcana-clues/', RandomArcanaCluesView.as_view(), name='arcana-clues'),
    # path('fin_anti_code/', FinancialAndAntiCodeByBirthDateView.as_view(), name='fin_anti_code'),
    # path('yes-no-maybe/', YesNoMaybeAnswerView.as_view(), name='yes-no-maybe'),
]