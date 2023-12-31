# Generated by Django 4.2.1 on 2023-05-31 22:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_todoitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todoitem",
            old_name="list",
            new_name="todo_list_list",
        ),
        migrations.AlterField(
            model_name="todoitem",
            name="due_date",
            field=models.DateTimeField(null=True),
        ),
    ]
