from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='read',
            new_name='is_read',
        ),
    ]
