# Generated by Django 3.2.19 on 2023-05-09 12:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tools", "0036_merge_20230504_1629"),
        ("tools", "0033_alter_organization_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="organization",
            options={
                "permissions": (
                    ("can_switch_organization", "Can switch organization"),
                    ("can_scan_organization", "Can scan organization"),
                    ("can_enable_disable_boefje", "Can enable or disable boefje"),
                    ("can_set_clearance_level", "Can set clearance level"),
                    ("can_delete_oois", "Can delete oois"),
                    ("can_recalculate_bits", "Can recalculate bits"),
                )
            },
        ),
    ]
