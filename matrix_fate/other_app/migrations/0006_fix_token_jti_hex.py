# from uuid import UUID
# from django.db import migrations

# def fix_jti_hex(apps, schema_editor):
#     OutstandingToken = apps.get_model("token_blacklist", "OutstandingToken")


#     for token in OutstandingToken.objects.all():
#         try:
#             token.jti_hex = UUID(token.jti).hex
#             token.save()
#         except Exception:
#             continue  # можно добавить логирование

# class Migration(migrations.Migration):
#     dependencies = [
#         ("other_app", "0005_alter_accessmatrixmodel_description_and_more"),
#     ]

#     operations = [
#         migrations.RunPython(fix_jti_hex),
#     ]


from django.db import migrations

def fix_jti_hex(apps, schema_editor):
    try:
        OutstandingToken = apps.get_model("token_blacklist", "OutstandingToken")
    except LookupError:
        # если вдруг при создании базы Django не знает про token_blacklist
        return

    # Тут можешь оставить или закомментировать логику, если не важна при тестировании
    # for token in OutstandingToken.objects.all():
    #     # какое-то преобразование, если нужно
    #     pass

class Migration(migrations.Migration):

    dependencies = [
    ("other_app", "0005_alter_accessmatrixmodel_description_and_more"),
]


    operations = [
        migrations.RunPython(fix_jti_hex, reverse_code=migrations.RunPython.noop),
    ]
