from mongoengine import *

connect('developers')

class Project(Document):

    title = StringField(max_length=255)
    description = StringField(max_length=8192)
    deadline = DateField(required=True)

    def get_developers(self):
        return Developer.objects.filter(
            project=self
            )


class Developer(Document):

    POSITIONS = (
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('DBA', 'DBA')
    )

    fullname = StringField(min_length=3, required=True)
    position = StringField(min_length=0, choices=POSITIONS, required=True)
    project = ReferenceField(Project)


if __name__ == '__main__':
    import datetime
    positions = ('Backend', 'Frontend', 'DBA')

    # dev1 = Developer.objects.create(
    #     fullname = 'John Nickolson',
    #     position=positions[0]
    #     )

    # dev2 = Developer.objects.create(
    #     fullname='Johne Dep',
    #     position=positions[1]
    #     )

    project = Project.objects.create(
        title='Facebook',
        description='Social network',
        deadline=datetime.datetime.now()
        )

    dev1 = Developer.objects.create(
        fullname='Johne Dep222',
        position=positions[1],
        project=project
        )