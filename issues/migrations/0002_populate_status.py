from django.db import migrations

def populate_status(apps, schema_editor):
    Status = apps.get_model('issues', 'Status')
    statuses = [
        {'name': 'To Do', 'description': 'Issue has been created but not started'},
        {'name': 'In Progress', 'description': 'Issue is currently being worked on'},
        {'name': 'Done', 'description': 'Issue has been completed'},
    ]
    for status in statuses:
        Status.objects.create(**status)

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]