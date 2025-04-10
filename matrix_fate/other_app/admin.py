# from django.contrib import admin
# from django.contrib.admin import AdminSite
# from .models import (

#     AccessMatrixModel,

#     FinancialAndAntiCodeCalculation, ArcanaClues, PastCard, PresentCard, FutureCard, 

#     MessageSupport, PublicOfferAgreement, PrivacyPolicy,

#     LandingPage,
# )


# class MatrixAdmin(AdminSite):
#     site_header = "Управление данными для матрицы Прогнозов"
#     site_title = "Админ панель Матрицы Прогнозов"
#     index_title = "Добро пожаловать в админ панель Матрицы Прогнозов"

#     def get_app_list(self, request):
#         """Группировка моделей без стандартных категорий"""

#         grouped_apps = [
#             ("ДОП РАСЧЕТЫ", [
#                 "FinancialAndAntiCodeCalculation", "ArcanaClues", "PastCard", "PresentCard", "FutureCard"]
#             ),
#             ("ОСТАЛЬНЫЕ", [
#                 "AccessMatrixModel", "MessageSupport", "PublicOfferAgreement", "PrivacyPolicy",
#                 "LandingPage"]
#             ),
#         ]

#         grouped_models = {group[0]: {"name": group[0], "models": []} for group in grouped_apps}

#         registered_models = {model.__name__: model for model in self._registry}

#         for group_name, model_names in grouped_apps:
#             for model_name in model_names:
#                 if model_name in registered_models:
#                     model = registered_models[model_name]
#                     grouped_models[group_name]["models"].append({
#                         "name": model._meta.verbose_name_plural,
#                         "object_name": model.__name__,
#                         "admin_url": f"/prognosis_admin/{model._meta.app_label.lower()}/{model.__name__.lower()}/"
#                     })

#         return [grouped_models[group] for group in grouped_models if grouped_models[group]["models"]]


# prognosis_admin = MatrixAdmin(name="prognosis_admin")


# class BaseAdmin(admin.ModelAdmin):
#     list_display = ("id", "order_id", "title", "description")
#     search_fields = ("order_id", "title")
#     list_filter = ("id",)
#     list_per_page = 22
#     list_display_links = ("order_id", "title", "description")


# for model in [AccessMatrixModel, LandingPage, FinancialAndAntiCodeCalculation, 
#               ArcanaClues, PastCard, PresentCard, FutureCard, MessageSupport, 
#               PublicOfferAgreement, PrivacyPolicy,
#     ]:
#     prognosis_admin.register(model, BaseAdmin)


