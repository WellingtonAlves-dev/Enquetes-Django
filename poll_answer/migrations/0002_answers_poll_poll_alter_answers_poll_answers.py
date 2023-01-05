# Generated by Django 4.1.4 on 2022-12-24 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_polls_description_remove_polls_options_and_more'),
        ('poll_answer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers_poll',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.polls'),
        ),
        migrations.AlterField(
            model_name='answers_poll',
            name='answers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.options'),
        ),
    ]