# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 11:46
from __future__ import unicode_literals

import json

from django.db import migrations


def populate_workpage_authors(apps, schema_editor):
    WorkPageAuthor = apps.get_model('work.WorkPageAuthor')
    Author = apps.get_model('people.Author')

    # Update model
    for work_page_author in WorkPageAuthor.objects.iterator():
        if work_page_author.author_person_page is None:
            continue

        work_page_author.author = Author.objects.get(person_page=work_page_author.author_person_page)
        work_page_author.save()

    # Update revisions
    PageRevision = apps.get_model('wagtailcore.PageRevision')
    ContentType = apps.get_model('contenttypes.ContentType')
    work_page_content_type = ContentType.objects.get(app_label='work', model='workpage')

    for revision in PageRevision.objects.filter(page__content_type=work_page_content_type):
        content = json.loads(revision.content_json)

        for author in content.get('related_author', []):
            author_obj = Author.objects.filter(person_page_id=author['author']).first()

            author['author_person_page'] = author['author']
            author['author'] = author_obj.id if author_obj is not None else None

        revision.content_json = json.dumps(content)
        revision.save()


def delete_null_authors(apps, schema_editor):
    WorkPageAuthor = apps.get_model('work.WorkPageAuthor')
    WorkPageAuthor.objects.filter(author__isnull=True).delete()


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_workpageauthor_author'),
        ('people', '0003_populate_authors'),
    ]

    operations = [
        migrations.RunPython(populate_workpage_authors, nooperation),
        migrations.RunPython(delete_null_authors, nooperation),
    ]