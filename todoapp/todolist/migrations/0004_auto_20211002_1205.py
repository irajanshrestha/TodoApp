# Generated by Django 3.2.7 on 2021-10-02 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todolist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='Category',
            field=models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todolist.category'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2021-10-02'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2021-10-02'),
        ),
    ]
