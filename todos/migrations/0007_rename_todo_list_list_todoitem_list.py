# Generated by Django 4.2.1 on 2023-06-01 18:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0006_alter_todoitem_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todoitem",
            old_name="todo_list_list",
            new_name="list",
        ),
    ]
