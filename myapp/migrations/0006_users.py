# Generated by Django 4.2.3 on 2023-07-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_list_of_po_iteams_po_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('store_manager', 'Store Manager'), ('manager', 'Manager'), ('admin', 'Admin')], max_length=20)),
            ],
        ),
    ]