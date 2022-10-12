from datetime import date, datetime
from decimal import Clamped
from email.policy import default
from enum import unique
from optparse import Option
from random import choices
from statistics import mode
from tkinter import CASCADE
from django.db import models



class Employee_form(models.Model):
    clearance_type = [
        ('Annual Vacation إجازة سنوية ','Annual Vacation إجازة سنوية '),
        ('Compensatory Leave إجازة تعويضية','Compensatory Leave إجازة تعويضية'),
        ('End of Services  نهاية الخدمة','End of Services  نهاية الخدمة'),
        ('Assigned تكليف ','Assigned تكليف '),
        ('Shift نقل ','Shift نقل '),
        ('ايفاد','ايفاد'),
    ] 
    job_title = [
        ('Administrative Departments الأقسام الأدارية',(

            ('اداري','اداري'),
            ('Specialist اخصائي اداري','Specialist اخصائي اداري'),

        )),
       
       (' Medical Departments الأقسام الطبية ',(

            ('Specialist اخصائي طبيب','Specialist اخصائي طبيب'),
            ('Consultant استشاري','Consultant استشاري'),
            ('Resident مقيم','Resident مقيم'),

       )),

       ('Nursing Departments أقسام التمريض',(

            ('Specialist Nurse اخصائي تمريض','Specialist Nurse اخصائي تمريض'),

       )),
       
      
    ]
    department = [
        ('الصحة الالكترونية',(

            ('E-Health الصحة الإلكترونية ','E-Health الصحة الإلكترونية '),
        )),


        ('  مكافحة العدوى (التعقيم المركزي)',(

            ('التعقيم','التعقيم'),
            ('النفايات الطبية','النفايات الطبية'),

        )),
        
        ('التمريض Nursing',(

            ('Nursing Office مكتب التمريض ','Nursing Office مكتب التمريض '),
            ('(M1) الحوامل ','(M1) الحوامل '),
            ('(M2) ما بعد الولادة الطبيعية ','(M2) ما بعد الولادة الطبيعية '),
            (' (M3)ما بعد الولادة القيصرية ',' (M3)ما بعد الولادة القيصرية '),
            ('(DR) كشك الولادة ','(DR) كشك الولادة '),
            ('(OR) العمليات','(OR) العمليات'),
            ("ER الطوارئ","ER الطوارئ"),
            ('NICO عناية حديثي الولادة ','NICO عناية حديثي الولادة '),
            (' PICO عناية الأطفال ',' PICO عناية الأطفال '),
            ('Healthy Baby Unit وحدة الأطفال الأصحاء ','Healthy Baby Unit وحدة الأطفال الأصحاء '),
            ('ICU عناية الكبار ','ICU عناية الكبار '),
            ('Gynecology أمراض النساء ','Gynecology أمراض النساء '),
            ('OPD العيادات ','OPD العيادات '),
        )),
       
        ('الخدمات الطبية Medical Services',(

            ('OB-GYNEالنساءوالولادة','OB-GYNEالنساءوالولادة'),
            ('ICU العناية المركزة للكبار','ICU العناية المركزة للكبار'),
            ('PICOالعناية المركزة للأطفال','PICOالعناية المركزة للأطفال'),
            ('NICO العناية المركزة لحديثي الولادة','NICO العناية المركزة لحديثي الولادة'),
            ('التخديرAnestesia','التخديرAnestesia'),
            ('العلاج النفسي ','العلاج النفسي '),
            ('العمليات','العمليات'),
            ('باطنية الأطفال','باطنية الأطفال'),
            ('جراجة الاطفال','جراحة الاطفال'),
            ('إدارة الأسرة','إدارة الأسرة'),
            ('المراجعة الاكلينيكية','المراجعة الاكلينيكية'),
            ('الرعاية الصحية المنزلية','الرعاية الصحية المنزلية'),


        )),
       

        ('Support Medical Services الخدمات الطبية المساعدة ',(
            
            ('الرعاية الصيدلية ','الرعاية الصيدلية '),
            ('خدمات التغذية','خدمات التغذية'),
            ('التغذية السريريه','التغذية السريريه'),
            ('الاشعة','الاشعة'),
            ('المختبر و نقل الدم','المختبر و نقل الدم'),
            ('العلاج الطبيعي ','العلاج الطبيعي '),
            ('التوعية الدينية','التوعية الدينية'),



        )),

        (' الجودة و سلامة المرضى' , (

            ('الجودة وسلامة المرضى','الجودة وسلامة المرضى'),

        )),
        
        ('التواصل المؤسسي' , (

            ('التواصل المؤسسي','التواصل المؤسسي'),
        )),

        ('الشؤون الأكاديمية و التدريب', (

            ('الشؤون الأكاديمية و التدريب','الشؤون الأكاديمية و التدريب'),

        )),
      
        ('KPI التطوير و المشاريع ', (
            ('التطوير و المشاريع ','التطوير و المشاريع '),

        )),

        ('تنمية الإرادات',(

            ('تنمية الإرادات ','تنمية الإرادات '),

        )),

        ('الشؤون القانونية و الإلتزام',(

            ('الشؤون القانونية و الإلتزام','الشؤون القانونية و الإلتزام'),

        )),
       
        ('الإدارة المناوبة',(

            ('الادارة المناوبة','الادارة المناوبة'),
        )),

        ('تجربة المريض',(
            ('تجربة المريض','تجربة المريض'),

        )),
       
        ('الإمداد و التموين الطبي',(

            ('المستودعات الطبية','المستودعات الطبية'),
            ('المستودعات غير الطبية ','المستودعات غير الطبية '),
            ('التجهيزات','التجهيزات'),
            ('المشتريات','المشتريات'),
            ('العقود','العقود'),

        )),

        ('الموارد البشرية ',(

            ('الموارد البشرية','الموارد البشرية'),

        )),
       
        ('الشؤون المالية ',(

            ('الشؤون المالية','الشؤون المالية'),

        )),

        ('التشغيل',(

            ('التشغيل','التشغيل'),


        )),
        
      

        

    ]
    gender = [
        ('Female','Female'),
        ('Male','Male'),
        
    ]

    
    Full_Name = models.CharField(max_length=100 , null= True , blank=True)
    Clearance_Type = models.CharField(max_length=100, choices=clearance_type , null= True , blank=True)
    Acknowledgment_Number = models.IntegerField(null= True , blank=True)
    Start_Date = models.DateField(default=date.today(), blank=True)
    end_Date = models.DateField(default=date.today(), blank=True)
    Job_Title = models.CharField(max_length=100 ,choices=job_title , null= True , blank=True)
    Department = models.CharField(max_length=50, choices=department, null= True , blank=True)
    Employee_Number = models.IntegerField(null= True , blank=True)
    Gender = models.CharField(max_length=50,choices=gender, null= True , blank=True)
    Nationality = models.CharField(max_length=50, null= True , blank=True)
    Phone_Number = models.IntegerField(null= True , blank=True)
    Notes = models.TextField(null= True , blank=True)
    created = models.DateTimeField(default=datetime.now() , blank=True)
    FinalStat = models.CharField(default = 'pending', max_length=50, null= True , blank=True)
    classification = models.CharField(max_length=50, null= True , blank=True)
    f = models.FileField(upload_to='files', null= True , blank=True)
    


class Departments(models.Model):
    depa = [
        ('الصحة الالكترونية',(

            ('E-Health الصحة الإلكترونية ','E-Health الصحة الإلكترونية '),
        )),


        ('  مكافحة العدوى (التعقيم المركزي)' ,(

            ('التعقيم','التعقيم'),
            ('النفايات الطبية','النفايات الطبية'),

        )),
        
        ('التمريض Nursing',(

            ('Nursing Office مكتب التمريض ','Nursing Office مكتب التمريض '),
            ('(M1) الحوامل ','(M1) الحوامل '),
            ('(M2) ما بعد الولادة الطبيعية ','(M2) ما بعد الولادة الطبيعية '),
            (' (M3)ما بعد الولادة القيصرية ',' (M3)ما بعد الولادة القيصرية '),
            ('(DR) كشك الولادة ','(DR) كشك الولادة '),
            ('(OR) العمليات','(OR) العمليات'),
            ('ER الطوارئ','ER الطوارئ'),
            ('NICO عناية حديثي الولادة ','NICO عناية حديثي الولادة '),
            (' PICO عناية الأطفال ',' PICO عناية الأطفال '),
            ('Healthy Baby Unit وحدة الأطفال الأصحاء ','Healthy Baby Unit وحدة الأطفال الأصحاء '),
            ('ICU عناية الكبار ','ICU عناية الكبار '),
            ('Gynecology أمراض النساء ','Gynecology أمراض النساء '),
            ('OPD العيادات ','OPD العيادات '),
        )),
       
        ('الخدمات الطبية Medical Services',(

            ('OB-GYNEالنساءوالولادة','OB-GYNEالنساءوالولادة'),
            ('ICU العناية المركزة للكبار','ICU العناية المركزة للكبار'),
            ('PICOالعناية المركزة للأطفال','PICOالعناية المركزة للأطفال'),
            ('NICO العناية المركزة لحديثي الولادة','NICO العناية المركزة لحديثي الولادة'),
            ('التخديرAnestesia','التخديرAnestesia'),
            ('العلاج النفسي ','العلاج النفسي '),
            ('العمليات','العمليات'),
            ('باطنية الأطفال','باطنية الأطفال'),
            ('جراجة الاطفال','جراحة الاطفال'),
            ('إدارة الأسرة','إدارة الأسرة'),
            ('المراجعة الاكلينيكية','المراجعة الاكلينيكية'),
            ('الرعاية الصحية المنزلية','الرعاية الصحية المنزلية'),


        )),
       

        ('Support Medical Services الخدمات الطبية المساعدة ',(
            
            ('الرعاية الصيدلية ','الرعاية الصيدلية '),
            ('خدمات التغذية','خدمات التغذية'),
            ('التغذية السريريه','التغذية السريريه'),
            ('الاشعة','الاشعة'),
            ('المختبر و نقل الدم','المختبر و نقل الدم'),
            ('العلاج الطبيعي ','العلاج الطبيعي '),
            ('التوعية الدينية','التوعية الدينية'),



        )),

        (' الجودة و سلامة المرضى' , (

            ('الجودة وسلامة المرضى','الجودة وسلامة المرضى'),

        )),
        
        ('التواصل المؤسسي' , (

            ('التواصل المؤسسي','التواصل المؤسسي'),
        )),

        ('الشؤون الأكاديمية و التدريب', (

            ('الشؤون الأكاديمية و التدريب','الشؤون الأكاديمية و التدريب'),

        )),
      
        ('KPI التطوير و المشاريع ', (
            ('التطوير و المشاريع ','التطوير و المشاريع '),

        )),

        ('تنمية الإرادات',(

            ('تنمية الإرادات ','تنمية الإرادات '),

        )),

        ('الشؤون القانونية و الإلتزام',(

            ('الشؤون القانونية و الإلتزام','الشؤون القانونية و الإلتزام'),

        )),
       
        ('الإدارة المناوبة',(

            ('الادارة المناوبة','الادارة المناوبة'),
        )),

        ('تجربة المريض',(
            ('تجربة المريض','تجربة المريض'),

        )),
       
        ('الإمداد و التموين الطبي',(

            ('المستودعات الطبية','المستودعات الطبية'),
            ('المستودعات غير الطبية ','المستودعات غير الطبية '),
            ('التجهيزات','التجهيزات'),
            ('المشتريات','المشتريات'),
            ('العقود','العقود'),

        )),

        ('الموارد البشرية ',(

            ('الموارد البشرية','الموارد البشرية'),

        )),
       
        ('الشؤون المالية ',(

            ('الشؤون المالية','الشؤون المالية'),

        )),

        ('التشغيل',(

            ('التشغيل','التشغيل'),


        )),

    ]

    DD = models.ForeignKey(Employee_form,max_length=100, choices=depa, blank=True, null=True, on_delete=models.PROTECT)
  


class dept_sign(models.Model):
    Email = models.CharField(max_length=100)
    password = models.TextField


class Nursing(models.Model):
    Option1 = [
        ('pending','pending'),
        ('approved','approved'),
        ('rejection','rejection'),
    ]
    
    IdOrder = models.IntegerField(null=True , blank=True)
    Option_dep = models.CharField(default='pending',max_length=50,choices=Option1, null= True , blank=True)
    Path = models.CharField(default='pending', max_length=100, null= True , blank=True)
    NumJob = models.IntegerField(null=True , blank=True)
    NameUser = models.CharField(max_length=100,null= True , blank=True)
    State = models.BooleanField(default=False,null= True , blank=True)
    Notes = models.TextField(null= True , blank=True)
    Username = models.CharField(max_length=20,null= True , blank=True )
    created = models.DateTimeField(default=datetime.now() , blank=True)
    
        
        
class Doctor(models.Model):
    Option1 = [
        ('pending','pending'),
        ('approved','approved'),
        ('rejection','rejection'),
        
    ]
    IdOrder = models.IntegerField(null=True , blank=True)
    Option_dep = models.CharField(default='pending',max_length=50,choices=Option1, null= True , blank=True)
    Path = models.CharField(max_length=100, null= True , blank=True)
    NumJob = models.IntegerField(null=True , blank=True)
    NameUser = models.CharField(max_length=100,null= True , blank=True)
    State = models.BooleanField(default=False,null= True , blank=True)
    Notes = models.TextField(null= True , blank=True)
    Username = models.CharField(max_length=20,null= True , blank=True )
    created = models.DateTimeField(default=datetime.now() , blank=True)
    
        
        
class Administrator(models.Model):
    Option1 = [
        ('pending','pending'),
        ('approved','approved'),
        ('rejection','rejection'),
    ]

    IdOrder = models.IntegerField(null=True , blank=True)
    Option_dep = models.CharField(default='pending',max_length=50,choices=Option1, null= True , blank=True)
    Path = models.CharField(max_length=100, null= True , blank=True)
    NumJob = models.IntegerField(null=True , blank=True)
    NameUser = models.CharField(max_length=100,null= True , blank=True)
    State = models.BooleanField(default=False,null= True , blank=True)
    Notes = models.TextField(null= True , blank=True)
    Username = models.CharField(max_length=20,null= True , blank=True )
    created = models.DateTimeField(default=datetime.now() , blank=True)
    
        

