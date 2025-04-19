from django.core.management.base import BaseCommand
from django.utils.html import escape
from child_app.models import (
    ChildCategory,
    ChildBusinessCard,
    QualitiesRevealedAgeOf20, ThirdTalentRevealedAge40,
    ChildOpportunity,
    ChildPointOfComfort,
    MainTaskSoul, SoulPastExperiencesWithPeople, LessonsFromPastLife,
    ChildDestinyArcana1, ChildDestinyArcana2, ChildDestinyArcana3,
    WhatChildShouldTeachParents, WhatMistakesRelationshipParentsChildren, WhatShouldComeQualitiesChild,
)


CATEGORY_MAPPING = {
    "Lapsen synnynnäinen lahjakkuus": 1,
    "Henkilökohtaiset ominaisuudet": 2,
    "Lapsen itsensä toteuttaminen": 3,
    "Lapsen sielullisen mukavuuden piste": 4,
    "Aiemmilta vuosilta jatkuvat tehtävät": 5,
    "Lapsen elämäntehtävä": 6,
    "Lapsi–vanhempi-karma": 7,
    "Ohjelmoinnit / Mentaaliset ohjelmat": 8,
}

DESCRIPTION = "Tässä pitäisi olla kuvaus"


def create_entries(model, category_id, title_prefix, description_prefix):
    category = ChildCategory.objects.get(id=category_id)
    entries = [
        model(
            category=category,
            title=f"{title_prefix} {i}",
            description=escape(f"{description_prefix} {i}"),
            order_id=i,
        ) for i in range(1, 23)
    ]
    model.objects.bulk_create(entries)

class Command(BaseCommand):
    help = "Заполняет таблицы данными"

    def handle(self, *args, **kwargs):
        create_entries(ChildBusinessCard, CATEGORY_MAPPING["Lapsen synnynnäinen lahjakkuus"], "Lapsen käyntikortti", DESCRIPTION)
        create_entries(QualitiesRevealedAgeOf20, CATEGORY_MAPPING["Henkilökohtaiset ominaisuudet"], "20 ikävuoteen mennessä ilmenevät ominaisuudet", DESCRIPTION)
        create_entries(ThirdTalentRevealedAge40, CATEGORY_MAPPING["Henkilökohtaiset ominaisuudet"], "Kolmas lahjakkuus paljastuu 40 ikävuoteen mennessä", DESCRIPTION)
        create_entries(ChildOpportunity, CATEGORY_MAPPING["Lapsen itsensä toteuttaminen"], "Lapsen mahdollisuus", DESCRIPTION)
        create_entries(ChildPointOfComfort, CATEGORY_MAPPING["Lapsen sielullisen mukavuuden piste"], "Arcan", DESCRIPTION)
        create_entries(MainTaskSoul, CATEGORY_MAPPING["Aiemmilta vuosilta jatkuvat tehtävät"], "Sielun päätehtävä", DESCRIPTION)
        create_entries(SoulPastExperiencesWithPeople, CATEGORY_MAPPING["Aiemmilta vuosilta jatkuvat tehtävät"], "Sielun kokemus menneisyydessä ihmisten kanssa", DESCRIPTION)
        create_entries(LessonsFromPastLife, CATEGORY_MAPPING["Aiemmilta vuosilta jatkuvat tehtävät"], "Oppitunti menneestä elämästä", DESCRIPTION)
        create_entries(ChildDestinyArcana1, CATEGORY_MAPPING["Lapsen elämäntehtävä"], "Arcan1", DESCRIPTION)
        create_entries(ChildDestinyArcana2, CATEGORY_MAPPING["Lapsen elämäntehtävä"], "Arcan2", DESCRIPTION)
        create_entries(ChildDestinyArcana3, CATEGORY_MAPPING["Lapsen elämäntehtävä"], "Arcan3", DESCRIPTION)
        create_entries(WhatChildShouldTeachParents, CATEGORY_MAPPING["Lapsi–vanhempi-karma"], "Mitä lapsen tulisi opettaa vanhemmilleen", DESCRIPTION)
        create_entries(WhatMistakesRelationshipParentsChildren, CATEGORY_MAPPING["Lapsi–vanhempi-karma"], "Mitä virheitä voit tehdä suhteessasi vanhempiesi ja lastesi kanssa", DESCRIPTION)
        create_entries(WhatShouldComeQualitiesChild, CATEGORY_MAPPING["Lapsi–vanhempi-karma"], "Mihin pitäisi tulla, mitä ominaisuuksia lapsen on rakennettava", DESCRIPTION)

        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))

# python manage.py fill_child_data

