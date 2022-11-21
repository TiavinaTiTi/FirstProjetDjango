# Generated by Django 4.0.5 on 2022-06-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, choices=[('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré')], null=True)),
            ],
        ),
    ]
