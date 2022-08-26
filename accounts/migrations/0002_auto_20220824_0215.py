from django.db import migrations

def populate_roles(apps, schemaeditor):
    roles = {
        "reader": "A person a subscription to our newspaper",
        "journalist": "A person that writes journalistic content",
        "columnist": "A person that creates columns for the newspaper",
        "editor": "A person who can edit or publish articles"
    }
    Role = apps.get_model("accounts", "Role")
    for name, desc in roles.items():
        role_obj = Role(name=name, description=desc)
        role_obj.save()

def populate_dept(apps, schemaeditor):
    depts = {
        "Headlines": "Important recent events",
        "Sports": "News related to sporting events",
        "Society": "News related to people in your community",
        "Business": "News related to businesses, stock prices, etc.",
        "Politics": "News related to politics",
    }
    Department = apps.get_model("accounts", "Department")
    for name, desc in depts.items():
        dept_obj = Department(name=name, description=desc)
        dept_obj.save()

class Migration(migrations.Migration):
    dependencies=[
        ("accounts", "0001_initial"),
    ]

    operations=[
        migrations.RunPython(populate_roles),
        migrations.RunPython(populate_dept),
    ]