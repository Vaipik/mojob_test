import factory.fuzzy

from ..models import Job, JobHeader


class JobFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText
    type = factory.fuzzy.FuzzyChoice(Job.JobTypeChoices.choices)

    class Meta:
        model = Job


class JobHeaderFactory(factory.django.DjangoModelFactory):
    rich_title_text = factory.fuzzy.FuzzyText(
        prefix=r"</b>",
        length=12,
        suffix=r"</b>"
    )
    rich_subtitle_text = factory.fuzzy.FuzzyText(
        prefix=r"</b>",
        length=12,
        suffix=r"</b>"
    )

    job = factory.SubFactory(JobFactory)

    class Meta:
        model = JobHeader
