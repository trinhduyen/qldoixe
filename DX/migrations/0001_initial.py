# Generated by Django 4.0.1 on 2022-02-11 03:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameDv', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='groupmaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameNVT', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='groupthietbi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameGroupTB', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdVT', models.CharField(max_length=255, unique=True)),
                ('NameVT', models.CharField(max_length=255, unique=True)),
                ('IdDV', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.dv')),
                ('IdNVTF', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.groupmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaNV', models.CharField(max_length=255, unique=True)),
                ('TenNV', models.CharField(max_length=255)),
                ('TuoiNV', models.IntegerField()),
                ('Namlv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Xe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BienSoXe', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='XeVao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sophieu', models.UUIDField(default=uuid.uuid4)),
                ('datetimeXevao', models.DateTimeField()),
                ('datetimeXera', models.DateTimeField(blank=True)),
                ('LyDoXeVao', models.TextField(max_length=500)),
                ('Lydo', models.TextField(max_length=500)),
                ('BienSoXe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.xe')),
                ('NhanVienPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.nhanvien')),
            ],
        ),
        migrations.CreateModel(
            name='VatTuDung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dongia', models.FloatField()),
                ('SoLuong', models.PositiveIntegerField()),
                ('thanhtien', models.FloatField()),
                ('TrangThaiKho', models.CharField(choices=[('Có', 'Có'), ('Không', 'Không')], max_length=50)),
                ('TrangThaiXuat', models.CharField(choices=[('Chưa Xuất', 'Chưa Xuất'), ('Đã Xuất', 'Đã Xuất')], max_length=50)),
                ('DatetimeXuat', models.DateTimeField(blank=True)),
                ('VtSudung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.material')),
                ('XeVao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.xevao')),
            ],
        ),
        migrations.CreateModel(
            name='thietbi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameTB', models.CharField(max_length=255, unique=True)),
                ('IdGroupTB', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DX.groupthietbi')),
            ],
        ),
    ]
