# Generated by Django 4.1.1 on 2022-09-26 11:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept_sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option_dep', models.CharField(blank=True, choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], max_length=50, null=True)),
                ('Path_Doctor', models.CharField(blank=True, choices=[('المساعد للخدمات الطبية Assistant Medical Servies', 'المساعد للخدمات الطبية Assistant Medical Servies'), ('رئيس القسم Head of Department', 'رئيس القسم Head of Department'), ('المالية Finaneial Dept', 'المالية Finaneial Dept'), ('الشؤون القانونية والالتزام Legal affairs', 'الشؤون القانونية والالتزام Legal affairs'), ('مراقبة المخزون Controlling Dept', 'مراقبة المخزون Controlling Dept'), ('الامن الصحي Health security', 'الامن الصحي Health security'), ('صحة العاملين Employee Clinic', 'صحة العاملين Employee Clinic'), ('الموارد البشرية Human Resourse', 'الموارد البشرية Human Resourse'), ('إدارة السكن Housing Management ', 'إدارة السكن Housing Management'), ('الصيدلية Pharmacy Dept', 'الصيدلية Pharmacy Dept'), ('الصحة الالكترونية Information Technology', 'الصحة الالكترونية Information Technology'), ('مراقبة انتظام دوام الموارد البشرية Monitoring the regularity of human resources', 'مراقبة انتظام دوام الموارد البشرية Monitoring the regularity of human resources'), ('شؤون المرضى Patient affairs', 'شؤون المرضى Patient affairs')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Clearance_Type', models.CharField(blank=True, choices=[('Annual Vacation إجازة سنوية ', 'Annual Vacation إجازة سنوية '), ('Compensatory Leave إجازة تعويضية', 'Compensatory Leave إجازة تعويضية'), ('End of Services  نهاية الخدمة', 'End of Services  نهاية الخدمة'), ('Assigned تكليف ', 'Assigned تكليف '), ('Shift نقل ', 'Shift نقل '), ('ايفاد', 'ايفاد')], max_length=100, null=True)),
                ('Acknowledgment_Number', models.IntegerField(blank=True, null=True)),
                ('Start_Date', models.DateField(blank=True, default=datetime.date(2022, 9, 26))),
                ('end_Date', models.DateField(blank=True, default=datetime.date(2022, 9, 26))),
                ('Job_Title', models.CharField(blank=True, choices=[('Administrative Departments الأقسام الأدارية', (('اداري', 'اداري'), ('Specialist اخصائي', 'Specialist اخصائي'))), (' Medical Departments الأقسام الطبية ', (('Specialist اخصائي', 'Specialist اخصائي'), ('Consultant استشاري', 'Consultant استشاري'), ('Resident مقيم', 'Resident مقيم'))), ('Nursing Departments أقسام التمريض', (('Specialist Nurse اخصائي تمريض', 'Specialist Nurse اخصائي تمريض'),))], max_length=100, null=True)),
                ('Department', models.CharField(blank=True, choices=[('الصحة الالكترونية', (('E-Health الصحة الإلكترونية ', 'E-Health الصحة الإلكترونية '),)), ('  مكافحة العدوى (التعقيم المركزي)', (('التعقيم', 'التعقيم'), ('النفايات الطبية', 'النفايات الطبية'))), ('التمريض Nursing', (('Nursing Office مكتب التمريض ', 'Nursing Office مكتب التمريض '), ('(M1) الحوامل ', '(M1) الحوامل '), ('(M2) ما بعد الولادة الطبيعية ', '(M2) ما بعد الولادة الطبيعية '), (' (M3)ما بعد الولادة القيصرية ', ' (M3)ما بعد الولادة القيصرية '), ('(DR) كشك الولادة ', '(DR) كشك الولادة '), ('(OR) العمليات', '(OR) العمليات'), ('ER الطوارئ ', 'ER الطوارئ '), ('NICO عناية حديثي الولادة ', 'NICO عناية حديثي الولادة '), (' PICO عناية الأطفال ', ' PICO عناية الأطفال '), ('Healthy Baby Unit وحدة الأطفال الأصحاء ', 'Healthy Baby Unit وحدة الأطفال الأصحاء '), ('ICU عناية الكبار ', 'ICU عناية الكبار '), ('Gynecology أمراض النساء ', 'Gynecology أمراض النساء '), ('OPD العيادات ', 'OPD العيادات '))), ('الخدمات الطبية Medical Services', (('OB-GYNEالنساءوالولادة', 'OB-GYNEالنساءوالولادة'), ('ICU العناية المركزة للكبار', 'ICU العناية المركزة للكبار'), ('PICOالعناية المركزة للأطفال', 'PICOالعناية المركزة للأطفال'), ('NICO العناية المركزة لحديثي الولادة', 'NICO العناية المركزة لحديثي الولادة'), ('التخديرAnestesia', 'التخديرAnestesia'), ('العلاج النفسي ', 'العلاج النفسي '), ('العمليات', 'العمليات'), ('باطنية الأطفال', 'باطنية الأطفال'), ('جراجة الاطفال', 'جراحة الاطفال'), ('إدارة الأسرة', 'إدارة الأسرة'), ('المراجعة الاكلينيكية', 'المراجعة الاكلينيكية'), ('الرعاية الصحية المنزلية', 'الرعاية الصحية المنزلية'))), ('Support Medical Services الخدمات الطبية المساعدة ', (('الرعاية الصيدلية ', 'الرعاية الصيدلية '), ('خدمات التغذية', 'خدمات التغذية'), ('التغذية السريريه', 'التغذية السريريه'), ('الاشعة', 'الاشعة'), ('المختبر و نقل الدم', 'المختبر و نقل الدم'), ('العلاج الطبيعي ', 'العلاج الطبيعي '), ('التوعية الدينية', 'التوعية الدينية'))), (' الجودة و سلامة المرضى', (('الجودة وسلامة المرضى', 'الجودة وسلامة المرضى'),)), ('التواصل المؤسسي', (('التواصل المؤسسي', 'التواصل المؤسسي'),)), ('الشؤون الأكاديمية و التدريب', (('الشؤون الأكاديمية و التدريب', 'الشؤون الأكاديمية و التدريب'),)), ('KPI التطوير و المشاريع ', (('التطوير و المشاريع ', 'التطوير و المشاريع '),)), ('تنمية الإرادات', (('تنمية الإرادات ', 'تنمية الإرادات '),)), ('الشؤون القانونية و الإلتزام', (('الشؤون القانونية و الإلتزام', 'الشؤون القانونية و الإلتزام'),)), ('الإدارة المناوبة', (('الادارة المناوبة', 'الادارة المناوبة'),)), ('تجربة المريض', (('تجربة المريض', 'تجربة المريض'),)), ('الإمداد و التموين الطبي', (('المستودعات الطبية', 'المستودعات الطبية'), ('المستودعات غير الطبية ', 'المستودعات غير الطبية '), ('التجهيزات', 'التجهيزات'), ('المشتريات', 'المشتريات'), ('العقود', 'العقود'))), ('الموارد البشرية ', (('الموارد البشرية', 'الموارد البشرية'),)), ('الشؤون المالية ', (('الشؤون المالية', 'الشؤون المالية'),)), ('التشغيل', (('التشغيل', 'التشغيل'),))], max_length=50, null=True)),
                ('Employee_Number', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone_Number', models.IntegerField(blank=True, null=True)),
                ('Notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 26, 13, 21, 26, 538962))),
            ],
        ),
        migrations.CreateModel(
            name='Nursing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option_dep', models.CharField(blank=True, choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], max_length=50, null=True)),
                ('Path_Nursing', models.CharField(blank=True, choices=[('رئيسة التمريض Nursing director', 'رئيسة التمريض Nursing director'), ('رئيس القسم Head of Department', 'رئيس القسم Head of Department'), ('المالية Finaneial Dept', 'المالية Finaneial Dept'), ('الشؤون القانونية والالتزام Legal affairs', 'الشؤون القانونية والالتزام Legal affairs'), ('مراقبة المخزون Controlling Dept', 'مراقبة المخزون Controlling Dept'), ('الامن الصحي Health security', 'الامن الصحي Health security'), ('صحة العاملين Employee Clinic', 'صحة العاملين Employee Clinic'), ('الموارد البشرية Human Resourse', 'الموارد البشرية Human Resourse'), ('إدارة السكن Housing Management ', 'إدارة السكن Housing Management'), ('الصيدلية Pharmacy Dept', 'الصيدلية Pharmacy Dept'), ('الصحة الالكترونية Information Technology', 'الصحة الالكترونية Information Technology'), ('مراقبة انتظام دوام الموارد البشرية Monitoring the regularity of human resources', 'مراقبة انتظام دوام الموارد البشرية Monitoring the regularity of human resources'), ('شؤون المرضى Patient affairs', 'شؤون المرضى Patient affairs')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option_dep', models.CharField(blank=True, choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], max_length=50, null=True)),
                ('Path_Administrators', models.CharField(blank=True, choices=[('رئيس القسم Head of Department', 'رئيس القسم Head of Department'), ('المالية Finaneial Dept', 'المالية Finaneial Dept'), ('الشؤون القانونية والالتزام Legal affairs', 'الشؤون القانونية والالتزام Legal affairs'), ('مراقبة المخزون Controlling Dept', 'مراقبة المخزون Controlling Dept'), ('الامن   security', 'الامن   security'), ('الصحة الالكترونية Information Technology', 'الصحة الالكترونية Information Technology'), ('صحة العاملين Employee Clinic', 'صحة العاملين Employee Clinic'), ('الموارد البشرية Human Resourse', 'الموارد البشرية Human Resourse'), ('إدارة السكن Housing Management ', 'إدارة السكن Housing Management')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DD', models.ForeignKey(blank=True, choices=[('الصحة الالكترونية', (('E-Health الصحة الإلكترونية ', 'E-Health الصحة الإلكترونية '),)), ('  مكافحة العدوى (التعقيم المركزي)', (('التعقيم', 'التعقيم'), ('النفايات الطبية', 'النفايات الطبية'))), ('التمريض Nursing', (('Nursing Office مكتب التمريض ', 'Nursing Office مكتب التمريض '), ('(M1) الحوامل ', '(M1) الحوامل '), ('(M2) ما بعد الولادة الطبيعية ', '(M2) ما بعد الولادة الطبيعية '), (' (M3)ما بعد الولادة القيصرية ', ' (M3)ما بعد الولادة القيصرية '), ('(DR) كشك الولادة ', '(DR) كشك الولادة '), ('(OR) العمليات', '(OR) العمليات'), ('ER الطوارئ ', 'ER الطوارئ '), ('NICO عناية حديثي الولادة ', 'NICO عناية حديثي الولادة '), (' PICO عناية الأطفال ', ' PICO عناية الأطفال '), ('Healthy Baby Unit وحدة الأطفال الأصحاء ', 'Healthy Baby Unit وحدة الأطفال الأصحاء '), ('ICU عناية الكبار ', 'ICU عناية الكبار '), ('Gynecology أمراض النساء ', 'Gynecology أمراض النساء '), ('OPD العيادات ', 'OPD العيادات '))), ('الخدمات الطبية Medical Services', (('OB-GYNEالنساءوالولادة', 'OB-GYNEالنساءوالولادة'), ('ICU العناية المركزة للكبار', 'ICU العناية المركزة للكبار'), ('PICOالعناية المركزة للأطفال', 'PICOالعناية المركزة للأطفال'), ('NICO العناية المركزة لحديثي الولادة', 'NICO العناية المركزة لحديثي الولادة'), ('التخديرAnestesia', 'التخديرAnestesia'), ('العلاج النفسي ', 'العلاج النفسي '), ('العمليات', 'العمليات'), ('باطنية الأطفال', 'باطنية الأطفال'), ('جراجة الاطفال', 'جراحة الاطفال'), ('إدارة الأسرة', 'إدارة الأسرة'), ('المراجعة الاكلينيكية', 'المراجعة الاكلينيكية'), ('الرعاية الصحية المنزلية', 'الرعاية الصحية المنزلية'))), ('Support Medical Services الخدمات الطبية المساعدة ', (('الرعاية الصيدلية ', 'الرعاية الصيدلية '), ('خدمات التغذية', 'خدمات التغذية'), ('التغذية السريريه', 'التغذية السريريه'), ('الاشعة', 'الاشعة'), ('المختبر و نقل الدم', 'المختبر و نقل الدم'), ('العلاج الطبيعي ', 'العلاج الطبيعي '), ('التوعية الدينية', 'التوعية الدينية'))), (' الجودة و سلامة المرضى', (('الجودة وسلامة المرضى', 'الجودة وسلامة المرضى'),)), ('التواصل المؤسسي', (('التواصل المؤسسي', 'التواصل المؤسسي'),)), ('الشؤون الأكاديمية و التدريب', (('الشؤون الأكاديمية و التدريب', 'الشؤون الأكاديمية و التدريب'),)), ('KPI التطوير و المشاريع ', (('التطوير و المشاريع ', 'التطوير و المشاريع '),)), ('تنمية الإرادات', (('تنمية الإرادات ', 'تنمية الإرادات '),)), ('الشؤون القانونية و الإلتزام', (('الشؤون القانونية و الإلتزام', 'الشؤون القانونية و الإلتزام'),)), ('الإدارة المناوبة', (('الادارة المناوبة', 'الادارة المناوبة'),)), ('تجربة المريض', (('تجربة المريض', 'تجربة المريض'),)), ('الإمداد و التموين الطبي', (('المستودعات الطبية', 'المستودعات الطبية'), ('المستودعات غير الطبية ', 'المستودعات غير الطبية '), ('التجهيزات', 'التجهيزات'), ('المشتريات', 'المشتريات'), ('العقود', 'العقود'))), ('الموارد البشرية ', (('الموارد البشرية', 'الموارد البشرية'),)), ('الشؤون المالية ', (('الشؤون المالية', 'الشؤون المالية'),)), ('التشغيل', (('التشغيل', 'التشغيل'),))], max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='em.employee_form')),
            ],
        ),
    ]
