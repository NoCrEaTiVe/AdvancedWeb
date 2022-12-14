# Generated by Django 3.2 on 2022-10-19 09:08

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.IntegerField()),
                ('add_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('max_score', models.IntegerField()),
                ('correct_option', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityStaff',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.customuser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('core.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('curator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='university.universitystaff')),
                ('specialization', models.ManyToManyField(to='university.Specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.customuser')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='university.studentgroup')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('core.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.courses')),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestionResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('exam_question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.examquestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student')),
            ],
        ),
        migrations.AddField(
            model_name='examquestion',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.exams'),
        ),
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='university.universitystaff'),
        ),
        migrations.CreateModel(
            name='CommentAppeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('appeal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.appeals')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customuser')),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.commentappeals')),
            ],
        ),
        migrations.AddField(
            model_name='appeals',
            name='appealed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student'),
        ),
    ]
