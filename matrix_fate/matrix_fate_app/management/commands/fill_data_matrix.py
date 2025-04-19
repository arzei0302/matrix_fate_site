from django.core.management.base import BaseCommand
from django.utils.html import escape
from matrix_fate_app.models import (
    Category,
    BirthTalent, YouthTalent, MatureTalent,
    InnateTalent, QualitiesRevealed, QualitiesDeveloped,
    MainTask40, TaskBefore40, TaskAfter40,
    SoulComfortPoint,
    SelfRealization,
    SoulMainTask, PastLifeExperience, PastLifeLesson,
    PersonalPowerPoint,
    AncestralPower,
    TeachParents, RelationshipMistakes, PersonalGrowth,
    SpiritualTask1, SpiritualTask2, SpiritualTask3,
    PartnerTasks, SuitablePartner, MeetingPlace, RelationshipProblems,

    SuitableProfessions, MoneySources, MoneyGrowthTasks1, MoneyGrowthTasks2, 
    MoneyBlocks, MoneyUnblock,

    PersonalPurpose1, PersonalPurpose2, PersonalPurpose3, SocialPurpose1, 
    SocialPurpose2, SocialPurpose3, SpiritualPurpose,

    PaternalDiseases, MaternalDiseases, HealthArcane1, HealthArcane2, HealthArcane3,
    AncestralTaskFatherFemale, AncestralTaskMotherFemale, AncestralTaskFatherMale, AncestralTaskMotherMale,

    SahasraraO7, SahasraraP7, SahasraraQ7,
    AdjnaO6, AdjnaP6, AdjnaQ6,
    VishudkhaO5, VishudkhaP5, VishudkhaQ5,
    AnakhataO4, AnakhataP4, AnakhataQ4,
    ManipuraO3, ManipuraP3, ManipuraQ3,
    SvadkhistanaO2, SvadkhistanaP2, SvadkhistanaQ2,
    MuladkharaO1, MuladkharaP1, MuladkharaQ1,
    TotalO, TotalP, TotalQ,
)

CATEGORY_MAPPING = {
    "Henkilökohtaiset ominaisuudet": 1,
    "Terveyskartta": 2,
    "Sieluntehtävä / Kutsumusammatti": 5,
    "Karma ja 40 vuoden tehtävä": 6,
    "Sielullisen mukavuuden piste": 7,
    "Itsensä toteuttaminen": 8,
    "Aiemmilta vuosilta jatkuvat tehtävät": 9,
    "Henkilökohtaisen voiman piste": 10,
    "Suvun voima": 11,
    "Lapsi–vanhempi-karma": 12,
    "Henkinen karma": 13,
    "Suhteet matriisissa": 14,
    "Raha matriisissa": 15,
    "Elämäntehtävä": 16,
    "Alttius sairauksille": 17,
    "Suvun tehtävät seitsemän sukupolvea taaksepäin": 18,
    # "Ohjelmoinnit / Mentaaliset ohjelmat": 19,
}

DESCRIPTION = "Tässä pitäisi olla kuvaus"


def create_entries(model, category_id, title_prefix, description_prefix):
    category = Category.objects.get(id=category_id)
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
        create_entries(BirthTalent, CATEGORY_MAPPING["Henkilökohtaiset ominaisuudet"], "Tärkein lahjakkuus, joka annetaan syntymässä", DESCRIPTION)
        create_entries(YouthTalent, CATEGORY_MAPPING["Henkilökohtaiset ominaisuudet"], "Toinen lahjakkuus paljastuu 20 ikävuoteen mennessä", DESCRIPTION)
        create_entries(MatureTalent, CATEGORY_MAPPING["Henkilökohtaiset ominaisuudet"], "Toinen lahjakkuus paljastuu 20 ikävuoteen mennessä", DESCRIPTION)

        create_entries(InnateTalent, CATEGORY_MAPPING["Sieluntehtävä / Kutsumusammatti"], "Suurin lahjakkuutesi syntymästä lähtien", DESCRIPTION)
        create_entries(QualitiesRevealed, CATEGORY_MAPPING["Sieluntehtävä / Kutsumusammatti"], "20 ikävuoteen mennessä ilmenevät ominaisuudet", DESCRIPTION)
        create_entries(QualitiesDeveloped, CATEGORY_MAPPING["Sieluntehtävä / Kutsumusammatti"], "Ominaisuudet, joita meidän on kehitettävä ennen 40 vuoden ikää", DESCRIPTION)

        create_entries(MainTask40, CATEGORY_MAPPING["Karma ja 40 vuoden tehtävä"], "Tärkein haaste 40 vuoden ajan", DESCRIPTION)
        create_entries(TaskBefore40, CATEGORY_MAPPING["Karma ja 40 vuoden tehtävä"], "Mitä sinun on tehtävä ennen kuin täytät 40", DESCRIPTION)
        create_entries(TaskAfter40, CATEGORY_MAPPING["Karma ja 40 vuoden tehtävä"], "Mitä sinun on tehtävä 40 ikävuoden jälkeen", DESCRIPTION)

        create_entries(SoulComfortPoint, CATEGORY_MAPPING["Sielullisen mukavuuden piste"], "Arcan", DESCRIPTION)

        create_entries(SelfRealization, CATEGORY_MAPPING["Itsensä toteuttaminen"], "Sinun tilaisuutesi", DESCRIPTION)

        create_entries(SoulMainTask, CATEGORY_MAPPING["Aiemmilta vuosilta jatkuvat tehtävät"], "Sielun päätehtävä", DESCRIPTION)
        create_entries(PastLifeExperience, CATEGORY_MAPPING["Aiemmilta vuosilta jatkuvat tehtävät"], "Sielusi aiemmat kokemukset ihmisten kanssa", DESCRIPTION)
        create_entries(PastLifeLesson, CATEGORY_MAPPING["Aiemmilta vuosilta jatkuvat tehtävät"], "Oppitunnit aiemmista elämistä", DESCRIPTION)

        create_entries(PersonalPowerPoint, CATEGORY_MAPPING["Henkilökohtaisen voiman piste"], "Noudata suosituksia", DESCRIPTION)

        create_entries(AncestralPower, CATEGORY_MAPPING["Suvun voima"], "Se on tehtävä", DESCRIPTION)

        create_entries(TeachParents, CATEGORY_MAPPING["Lapsi–vanhempi-karma"], "Mitä sinun olisi pitänyt opettaa vanhemmillesi", DESCRIPTION)
        create_entries(RelationshipMistakes, CATEGORY_MAPPING["Lapsi–vanhempi-karma"], "Mitä virheitä voi olla suhteissa vanhempiin ja heidän lapsiinsa", DESCRIPTION)
        create_entries(PersonalGrowth, CATEGORY_MAPPING["Lapsi–vanhempi-karma"], "Mitä pitäisi tulla, mitä ominaisuuksia on kehitettävä itsessään", DESCRIPTION)

        create_entries(SpiritualTask1, CATEGORY_MAPPING["Henkinen karma"], "Tehtävä1", DESCRIPTION)
        create_entries(SpiritualTask2, CATEGORY_MAPPING["Henkinen karma"], "Tehtävä2", DESCRIPTION)
        create_entries(SpiritualTask3, CATEGORY_MAPPING["Henkinen karma"], "Tehtävä3", DESCRIPTION)

        create_entries(PartnerTasks, CATEGORY_MAPPING["Suhteet matriisissa"], "Mitkä ovat haasteet kumppaneiden kanssa", DESCRIPTION)
        create_entries(SuitablePartner, CATEGORY_MAPPING["Suhteet matriisissa"], "Millainen kumppani sopii sinulle", DESCRIPTION)
        create_entries(MeetingPlace, CATEGORY_MAPPING["Suhteet matriisissa"], "Missä voit tavata kumppanisi", DESCRIPTION)
        create_entries(RelationshipProblems, CATEGORY_MAPPING["Suhteet matriisissa"], "Mitä parisuhdeongelmia voi syntyä", DESCRIPTION)

        create_entries(SuitableProfessions, CATEGORY_MAPPING["Raha matriisissa"], "Mitkä ovat oikeita ammatteja", DESCRIPTION)
        create_entries(MoneySources, CATEGORY_MAPPING["Raha matriisissa"], "Mikä antaa sinulle rahaa", DESCRIPTION)
        create_entries(MoneyGrowthTasks1, CATEGORY_MAPPING["Raha matriisissa"], "1Mitä tehtäviä sinun on suoritettava avataksesi rahakanavan", DESCRIPTION)
        create_entries(MoneyGrowthTasks2, CATEGORY_MAPPING["Raha matriisissa"], "2Mitä tehtäviä sinun on suoritettava avataksesi rahakanavan", DESCRIPTION)
        create_entries(MoneyBlocks, CATEGORY_MAPPING["Raha matriisissa"], "Mikä estää rahan energiaa", DESCRIPTION)
        create_entries(MoneyUnblock, CATEGORY_MAPPING["Raha matriisissa"], "Mikä auttaa vapauttamaan rahaa", DESCRIPTION)
    
        create_entries(PersonalPurpose1, CATEGORY_MAPPING["Elämäntehtävä"], "Henkilökohtaisen arkanan tehtävä1", DESCRIPTION)
        create_entries(PersonalPurpose2, CATEGORY_MAPPING["Elämäntehtävä"], "Henkilökohtaisen arkanan tehtävä2", DESCRIPTION)
        create_entries(PersonalPurpose3, CATEGORY_MAPPING["Elämäntehtävä"], "Henkilökohtaisen arkanan tehtävä3", DESCRIPTION)
        create_entries(SocialPurpose1, CATEGORY_MAPPING["Elämäntehtävä"], "Sosiaalisen arkanan tehtävä1", DESCRIPTION)
        create_entries(SocialPurpose2, CATEGORY_MAPPING["Elämäntehtävä"], "Sosiaalisen arkanan tehtävä2", DESCRIPTION)
        create_entries(SocialPurpose3, CATEGORY_MAPPING["Elämäntehtävä"], "Sosiaalisen arkanan tehtävä3", DESCRIPTION)
        create_entries(SpiritualPurpose, CATEGORY_MAPPING["Elämäntehtävä"], "Henkinen tarkoitus", DESCRIPTION)


        create_entries(PaternalDiseases, CATEGORY_MAPPING["Alttius sairauksille"], "Isän puolen perinnölliset sairaudet", DESCRIPTION)
        create_entries(MaternalDiseases, CATEGORY_MAPPING["Alttius sairauksille"], "Äidin synnynnäiset epämuodostumat", DESCRIPTION)
        create_entries(HealthArcane1, CATEGORY_MAPPING["Alttius sairauksille"], "Arcan1", DESCRIPTION)
        create_entries(HealthArcane2, CATEGORY_MAPPING["Alttius sairauksille"], "Arcan2", DESCRIPTION)
        create_entries(HealthArcane3, CATEGORY_MAPPING["Alttius sairauksille"], "Arcan3", DESCRIPTION)


        create_entries(AncestralTaskFatherFemale, CATEGORY_MAPPING["Suvun tehtävät seitsemän sukupolvea taaksepäin"], "Miesten sukujuuria koskevat tehtävät isän syntyperän mukaan", DESCRIPTION)
        create_entries(AncestralTaskMotherFemale, CATEGORY_MAPPING["Suvun tehtävät seitsemän sukupolvea taaksepäin"], "Miesten sukujuuria koskevat tehtävät äidin syntyperän mukaan", DESCRIPTION)
        create_entries(AncestralTaskFatherMale, CATEGORY_MAPPING["Suvun tehtävät seitsemän sukupolvea taaksepäin"], "Naisten sukujuuria koskevat tehtävät isän syntyperän mukaan", DESCRIPTION)
        create_entries(AncestralTaskMotherMale, CATEGORY_MAPPING["Suvun tehtävät seitsemän sukupolvea taaksepäin"], "Naisten sukujuuria koskevat tehtävät äidin syntyperän mukaan", DESCRIPTION)

        create_entries(SahasraraO7, CATEGORY_MAPPING["Terveyskartta"], "Kruunuchakra/Fysiikka", DESCRIPTION)
        create_entries(SahasraraP7, CATEGORY_MAPPING["Terveyskartta"], "Kruunuchakra/Energia", DESCRIPTION)
        create_entries(SahasraraQ7, CATEGORY_MAPPING["Terveyskartta"], "Kruunuchakra/Tunteet", DESCRIPTION)

        create_entries(AdjnaO6, CATEGORY_MAPPING["Terveyskartta"], "Kolmas silmä chakra/Fysiikka", DESCRIPTION)
        create_entries(AdjnaP6, CATEGORY_MAPPING["Terveyskartta"], "Kolmas silmä chakra/Energia", DESCRIPTION)
        create_entries(AdjnaQ6, CATEGORY_MAPPING["Terveyskartta"], "Kolmas silmä chakra/Tunteet", DESCRIPTION)

        create_entries(VishudkhaO5, CATEGORY_MAPPING["Terveyskartta"], "Kurkkuchakra/Fysiikka", DESCRIPTION)
        create_entries(VishudkhaP5, CATEGORY_MAPPING["Terveyskartta"], "Kurkkuchakra/Energia", DESCRIPTION)
        create_entries(VishudkhaQ5, CATEGORY_MAPPING["Terveyskartta"], "Kurkkuchakra/Tunteet", DESCRIPTION)

        create_entries(AnakhataO4, CATEGORY_MAPPING["Terveyskartta"], "Sydänckakra/Fysiikka", DESCRIPTION)
        create_entries(AnakhataP4, CATEGORY_MAPPING["Terveyskartta"], "Sydänckakra/Energia", DESCRIPTION)
        create_entries(AnakhataQ4, CATEGORY_MAPPING["Terveyskartta"], "Sydänckakra/Tunteet", DESCRIPTION)

        create_entries(ManipuraO3, CATEGORY_MAPPING["Terveyskartta"], "Aurinkopunoksen chakra/Fysiikka", DESCRIPTION)
        create_entries(ManipuraP3, CATEGORY_MAPPING["Terveyskartta"], "Aurinkopunoksen chakra/Energia", DESCRIPTION)
        create_entries(ManipuraQ3, CATEGORY_MAPPING["Terveyskartta"], "Aurinkopunoksen chakra/Tunteet", DESCRIPTION)

        create_entries(SvadkhistanaO2, CATEGORY_MAPPING["Terveyskartta"], "Sakraalichakra/Fysiikka", DESCRIPTION)
        create_entries(SvadkhistanaP2, CATEGORY_MAPPING["Terveyskartta"], "Sakraalichakra/Energia", DESCRIPTION)
        create_entries(SvadkhistanaQ2, CATEGORY_MAPPING["Terveyskartta"], "Sakraalichakra/Tunteet", DESCRIPTION)

        create_entries(MuladkharaO1, CATEGORY_MAPPING["Terveyskartta"], "Juurichakra/Fysiikka", DESCRIPTION)
        create_entries(MuladkharaP1, CATEGORY_MAPPING["Terveyskartta"], "Juurichakra/Energia", DESCRIPTION)
        create_entries(MuladkharaQ1, CATEGORY_MAPPING["Terveyskartta"], "Juurichakra/Tunteet", DESCRIPTION)

        create_entries(TotalO, CATEGORY_MAPPING["Terveyskartta"], "Yhteensä/Fysiikka", DESCRIPTION)
        create_entries(TotalP, CATEGORY_MAPPING["Terveyskartta"], "Yhteensä/Energia", DESCRIPTION)
        create_entries(TotalQ, CATEGORY_MAPPING["Terveyskartta"], "Yhteensä/Tunteet", DESCRIPTION)

        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))

# python manage.py fill_data_matrix