from multiprocessing import context
from sre_constants import BRANCH
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
import re
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'pages/index.html')


def emp_form(request):

    fullname = request.POST.get('fullname')
    eq = request.POST.get('eq')
    Clearance = request.POST.get('Clearance_Type')
    Start = request.POST.get('Start')
    end = request.POST.get('end')
    job = request.POST.get('Job_Title')
    department = request.POST.get('Department')
    EmployeeNumber = request.POST.get('EmployeeNumber')
    gender = request.POST.get('gender')
    Nationality = request.POST.get('Nationality')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')
    filename = request.POST.get('filename')

    if request.method == 'POST':
        if job in ['اداري', 'Specialist اخصائي اداري']:
            classific = 'Administrator'
        elif job == 'Specialist Nurse اخصائي تمريض':
            classific = 'Nursing'
        else:
            classific = 'Doctor'

        Employee_form(Full_Name=fullname,
                      Clearance_Type=Clearance,
                      Acknowledgment_Number=eq,
                      Start_Date=Start,
                      end_Date=end,
                      Job_Title=job,
                      Employee_Number=EmployeeNumber,
                      Department=department,
                      Gender=gender,
                      Nationality=Nationality,
                      Phone_Number=phone,
                      Notes=subject,
                      classification=classific,
                      f=filename,
                      ).save()
        step1 = Employee_form.objects.all()
        step2 = str(step1.reverse()[Employee_form.objects.count() - 1])
        step3 = re.findall(r'\d+', step2)
        IDN = int(step3[0])

        if job in ['اداري', 'Specialist اخصائي اداري']:
            Administrator.objects.create(
                NumJob=EmployeeNumber, NameUser=fullname, Path='HR', Username="HR", IdOrder=IDN).save()
            Administrator.objects.create(
                NumJob=EmployeeNumber, NameUser=fullname, Path='المالية Finaneial Dept', Username="Financial_Dept", IdOrder=IDN).save()
            Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون القانونية والالتزام Legal affairs', Username="Legal_affairs", IdOrder=IDN).save()
            Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='مراقبة المخزون Controlling Dept', Username="Controlling_Dept", IdOrder=IDN).save()
            Administrator.objects.create(
                NumJob=EmployeeNumber, NameUser=fullname, Path='الامن   security', Username="Security", IdOrder=IDN).save()
            Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الصحة الالكترونية Information Technology', Username="Information_Technology", IdOrder=IDN).save()
            Administrator.objects.create(
                NumJob=EmployeeNumber, NameUser=fullname, Path='صحة العاملين Employee Clinic', Username="Employee_Clinic", IdOrder=IDN).save()
            Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الموارد البشرية Human Resourse', Username="Human_Resource", IdOrder=IDN).save()
            Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='إدارة السكن Housing Management ', Username="Housing_Management", IdOrder=IDN).save()
            if department == 'E-Health الصحة الإلكترونية ':
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                                      Path='E-Health الصحة الإلكترونية ', Username="E_Health", IdOrder=IDN).save()
            elif department == 'التعقيم':
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التعقيم', Username="Central_sterilization", IdOrder=IDN).save() 
            elif department == 'النفايات الطبية':
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='النفايات الطبية', Username="Central_sterilization", IdOrder=IDN).save() 
            elif department == 'Nursing Office مكتب التمريض ':
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Nursing Office مكتب التمريض ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(M1) الحوامل ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(M1) الحوامل ', Username="Nursing", IdOrder=IDN).save()
            elif department == "(M2) ما بعد الولادة الطبيعية ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(M2) ما بعد الولادة الطبيعية ', Username="Nursing", IdOrder=IDN).save()
            elif department == " (M3)ما بعد الولادة القيصرية ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path=' (M3)ما بعد الولادة القيصرية ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(DR) كشك الولادة ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(DR) كشك الولادة ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(OR) العمليات":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(OR) العمليات', Username="Nursing", IdOrder=IDN).save() 
            elif department == "ER الطوارئ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path="ER الطوارئ", Username="Nursing", IdOrder=IDN).save()
            elif department == "NICO عناية حديثي الولادة ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='NICO عناية حديثي الولادة ', Username="Nursing", IdOrder=IDN).save() 
            elif department == " PICO عناية الأطفال ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path=' PICO عناية الأطفال ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "Healthy Baby Unit وحدة الأطفال الأصحاء ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Healthy Baby Unit وحدة الأطفال الأصحاء ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "ICU عناية الكبار ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='ICU عناية الكبار ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "Gynecology أمراض النساء ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Gynecology أمراض النساء ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "OPD العيادات ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='OPD العيادات  ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "OB-GYNEالنساءوالولادة":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='OB-GYNEالنساءوالولادة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "ICU العناية المركزة للكبار":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='ICU العناية المركزة للكبار', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "PICOالعناية المركزة للأطفال":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='PICOالعناية المركزة للأطفال', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "NICO العناية المركزة لحديثي الولادة":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='NICO العناية المركزة لحديثي الولادة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "التخديرAnestesia":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التخديرAnestesia', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "العلاج النفسي ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العلاج النفسي ', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "العمليات":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العمليات', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "باطنية الأطفال":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='باطنية الأطفال', Username="Medical_Services", IdOrder=IDN).save()
            elif department == "جراجة الاطفال":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='جراجة الاطفال', Username="Medical_Services", IdOrder=IDN).save()
            elif department == "إدارة الأسرة":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='إدارة الأسرة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "المراجعة الاكلينيكية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المراجعة الاكلينيكية', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "الرعاية الصحية المنزلية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الرعاية الصحية المنزلية', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "الرعاية الصيدلية ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الرعاية الصيدلية ', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "خدمات التغذية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='خدمات التغذية', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "التغذية السريريه":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التغذية السريريه', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "الاشعة":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الاشعة', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "المختبر و نقل الدم":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المختبر و نقل الدم', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "العلاج الطبيعي ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العلاج الطبيعي ', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "التوعية الدينية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التوعية الدينية', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "الجودة وسلامة المرضى":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الجودة وسلامة المرضى', Username="Quality_and_patient_safety", IdOrder=IDN).save() 
            elif department == "التواصل المؤسسي":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التواصل المؤسسي', Username="corporate_communication", IdOrder=IDN).save() 
            elif department == "الشؤون الأكاديمية و التدريب":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون الأكاديمية و التدريب', Username="Academic_Affairs_and_Training", IdOrder=IDN).save() 
            elif department == "التطوير و المشاريع ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التطوير و المشاريع ', Username="KPI", IdOrder=IDN).save() 
            elif department == "تنمية الإرادات":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='تنمية الإرادات', Username="revenue_development", IdOrder=IDN).save() 
            elif department == "الشؤون القانونية و الإلتزام":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون القانونية و الإلتزام', Username="Legal_Compliance", IdOrder=IDN).save() 
            elif department == "الادارة المناوبة":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الادارة المناوبة', Username="shift_management", IdOrder=IDN).save() 
            elif department == "تجربة المريض":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='تجربة المريض', Username="patient_experience", IdOrder=IDN).save() 
            elif department == "المستودعات الطبية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المستودعات الطبية', Username="Medical_supplies", IdOrder=IDN).save()
            elif department == "المستودعات غير الطبية ":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المستودعات غير الطبية ', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "التجهيزات":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التجهيزات', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "المشتريات":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المشتريات', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "العقود":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العقود', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "الموارد البشرية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الموارد البشرية', Username="HR", IdOrder=IDN).save() 
            elif department == "الشؤون المالية":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون المالية', Username="financial_affairs", IdOrder=IDN).save() 
            elif department == "التشغيل":
                 Administrator.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التشغيل', Username="Employment", IdOrder=IDN).save()   
            
            
        elif job == 'Specialist Nurse اخصائي تمريض':
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='HR', Username="HR", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='رئيسة التمريض Nursing director', Username="Nursing_director", IdOrder=IDN).save()
           
            Nursing.objects.create(
                NumJob=EmployeeNumber, NameUser=fullname, Path='المالية Finaneial Dept', Username="Financial_Dept", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='الشؤون القانونية والالتزام Legal affairs', Username="Legal_affairs", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='مراقبة المخزون Controlling Dept', Username="Controlling_Dept", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='الامن الصحي Health security', Username="Health_security", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='صحة العاملين Employee Clinic', Username="Employee_Clinic", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='الموارد البشرية Human Resourse', Username="Human_Resource", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='إدارة السكن Housing Management', Username="Housing_Management", IdOrder=IDN).save()
            Nursing.objects.create(
                NumJob=EmployeeNumber, NameUser=fullname, Path='الصيدلية Pharmacy Dept', Username="Pharmacy_Dept", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='مراقبة انتظام دوام الموارد البشرية Monitoring the regularity of human resources', Username="Monitoring_the_regularity_of_human_resources", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='الصحة الالكترونية Information Technology', Username="Information_Technology", IdOrder=IDN).save()
            Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                   Path='شؤون المرضى Patient affairs', Username="Patient_affairs", IdOrder=IDN).save()
            if department == 'E-Health الصحة الإلكترونية ':
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                                      Path='E-Health الصحة الإلكترونية ', Username="E_Health", IdOrder=IDN).save()
            elif department == 'التعقيم':
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التعقيم', Username="Central_sterilization", IdOrder=IDN).save() 
            elif department == 'النفايات الطبية':
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='النفايات الطبية', Username="Central_sterilization", IdOrder=IDN).save() 
            elif department == 'Nursing Office مكتب التمريض ':
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Nursing Office مكتب التمريض ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(M1) الحوامل ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(M1) الحوامل ', Username="Nursing", IdOrder=IDN).save()
            elif department == "(M2) ما بعد الولادة الطبيعية ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(M2) ما بعد الولادة الطبيعية ', Username="Nursing", IdOrder=IDN).save()
            elif department == " (M3)ما بعد الولادة القيصرية ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path=' (M3)ما بعد الولادة القيصرية ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(DR) كشك الولادة ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(DR) كشك الولادة ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(OR) العمليات":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(OR) العمليات', Username="Nursing", IdOrder=IDN).save() 
            elif department == "ER الطوارئ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path="ER الطوارئ", Username="Nursing", IdOrder=IDN).save()
            elif department == "NICO عناية حديثي الولادة ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='NICO عناية حديثي الولادة ', Username="Nursing", IdOrder=IDN).save() 
            elif department == " PICO عناية الأطفال ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path=' PICO عناية الأطفال ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "Healthy Baby Unit وحدة الأطفال الأصحاء ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Healthy Baby Unit وحدة الأطفال الأصحاء ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "ICU عناية الكبار ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='ICU عناية الكبار ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "Gynecology أمراض النساء ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Gynecology أمراض النساء ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "OPD العيادات ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='OPD العيادات  ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "OB-GYNEالنساءوالولادة":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='OB-GYNEالنساءوالولادة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "ICU العناية المركزة للكبار":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='ICU العناية المركزة للكبار', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "PICOالعناية المركزة للأطفال":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='PICOالعناية المركزة للأطفال', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "NICO العناية المركزة لحديثي الولادة":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='NICO العناية المركزة لحديثي الولادة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "التخديرAnestesia":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التخديرAnestesia', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "العلاج النفسي ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العلاج النفسي ', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "العمليات":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العمليات', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "باطنية الأطفال":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='باطنية الأطفال', Username="Medical_Services", IdOrder=IDN).save()
            elif department == "جراجة الاطفال":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='جراجة الاطفال', Username="Medical_Services", IdOrder=IDN).save()
            elif department == "إدارة الأسرة":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='إدارة الأسرة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "المراجعة الاكلينيكية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المراجعة الاكلينيكية', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "الرعاية الصحية المنزلية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الرعاية الصحية المنزلية', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "الرعاية الصيدلية ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الرعاية الصيدلية ', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "خدمات التغذية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='خدمات التغذية', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "التغذية السريريه":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التغذية السريريه', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "الاشعة":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الاشعة', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "المختبر و نقل الدم":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المختبر و نقل الدم', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "العلاج الطبيعي ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العلاج الطبيعي ', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "التوعية الدينية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التوعية الدينية', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "الجودة وسلامة المرضى":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الجودة وسلامة المرضى', Username="Quality_and_patient_safety", IdOrder=IDN).save() 
            elif department == "التواصل المؤسسي":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التواصل المؤسسي', Username="corporate_communication", IdOrder=IDN).save() 
            elif department == "الشؤون الأكاديمية و التدريب":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون الأكاديمية و التدريب', Username="Academic_Affairs_and_Training", IdOrder=IDN).save() 
            elif department == "التطوير و المشاريع ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التطوير و المشاريع ', Username="KPI", IdOrder=IDN).save() 
            elif department == "تنمية الإرادات":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='تنمية الإرادات', Username="revenue_development", IdOrder=IDN).save() 
            elif department == "الشؤون القانونية و الإلتزام":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون القانونية و الإلتزام', Username="Legal_Compliance", IdOrder=IDN).save() 
            elif department == "الادارة المناوبة":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الادارة المناوبة', Username="shift_management", IdOrder=IDN).save() 
            elif department == "تجربة المريض":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='تجربة المريض', Username="patient_experience", IdOrder=IDN).save() 
            elif department == "المستودعات الطبية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المستودعات الطبية', Username="Medical_supplies", IdOrder=IDN).save()
            elif department == "المستودعات غير الطبية ":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المستودعات غير الطبية ', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "التجهيزات":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التجهيزات', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "المشتريات":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المشتريات', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "العقود":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العقود', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "الموارد البشرية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الموارد البشرية', Username="HR", IdOrder=IDN).save() 
            elif department == "الشؤون المالية":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون المالية', Username="financial_affairs", IdOrder=IDN).save() 
            elif department == "التشغيل":
                 Nursing.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التشغيل', Username="Employment", IdOrder=IDN).save()   

        else:
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='HR', Username="HR", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='المساعد للخدمات الطبية Assistant Medical Servies', Username="Assistant_Medical_Servies", IdOrder=IDN).save()
            
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='المالية Finaneial Dept', Username="Financial_Dept", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='الشؤون القانونية والالتزام Legal affairs', Username="Legal_affairs", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='مراقبة المخزون Controlling Dept', Username="Controlling_Dept", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='الامن الصحي Health security', Username="Health_security", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='صحة العاملين Employee Clinic', Username="Employee_Clinic", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='الموارد البشرية Human Resourse', Username="Human_Resource", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='إدارة السكن Housing Management', Username="Housing_Management", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='الصيدلية Pharmacy Dept', Username="Pharmacy_Dept", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='مراقبة انتظام دوام الموارد البشرية Monitoring the regularity of human resources', Username="Monitoring_the_regularity_of_human_resources", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='الصحة الالكترونية Information Technology', Username="Information_Technology", IdOrder=IDN).save()
            Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                  Path='شؤون المرضى Patient affairs', Username="Patient_affairs", IdOrder=IDN).save()
            if department == 'E-Health الصحة الإلكترونية ':
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                                      Path='E-Health الصحة الإلكترونية ', Username="E_Health", IdOrder=IDN).save()
            elif department == 'التعقيم':
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التعقيم', Username="Central_sterilization", IdOrder=IDN).save() 
            elif department == 'النفايات الطبية':
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='النفايات الطبية', Username="Central_sterilization", IdOrder=IDN).save() 
            elif department == 'Doctor Office مكتب التمريض ':
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Doctor Office مكتب التمريض ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(M1) الحوامل ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(M1) الحوامل ', Username="Nursing", IdOrder=IDN).save()
            elif department == "(M2) ما بعد الولادة الطبيعية ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(M2) ما بعد الولادة الطبيعية ', Username="Nursing", IdOrder=IDN).save()
            elif department == " (M3)ما بعد الولادة القيصرية ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path=' (M3)ما بعد الولادة القيصرية ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(DR) كشك الولادة ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(DR) كشك الولادة ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "(OR) العمليات":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='(OR) العمليات', Username="Nursing", IdOrder=IDN).save() 
            elif department == "ER الطوارئ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path="ER الطوارئ", Username="Nursing", IdOrder=IDN).save()
            elif department == "NICO عناية حديثي الولادة ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='NICO عناية حديثي الولادة ', Username="Nursing", IdOrder=IDN).save() 
            elif department == " PICO عناية الأطفال ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path=' PICO عناية الأطفال ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "Healthy Baby Unit وحدة الأطفال الأصحاء ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Healthy Baby Unit وحدة الأطفال الأصحاء ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "ICU عناية الكبار ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='ICU عناية الكبار ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "Gynecology أمراض النساء ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='Gynecology أمراض النساء ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "OPD العيادات ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='OPD العيادات  ', Username="Nursing", IdOrder=IDN).save() 
            elif department == "OB-GYNEالنساءوالولادة":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='OB-GYNEالنساءوالولادة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "ICU العناية المركزة للكبار":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='ICU العناية المركزة للكبار', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "PICOالعناية المركزة للأطفال":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='PICOالعناية المركزة للأطفال', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "NICO العناية المركزة لحديثي الولادة":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='NICO العناية المركزة لحديثي الولادة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "التخديرAnestesia":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التخديرAnestesia', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "العلاج النفسي ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العلاج النفسي ', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "العمليات":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العمليات', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "باطنية الأطفال":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='باطنية الأطفال', Username="Medical_Services", IdOrder=IDN).save()
            elif department == "جراجة الاطفال":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='جراجة الاطفال', Username="Medical_Services", IdOrder=IDN).save()
            elif department == "إدارة الأسرة":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='إدارة الأسرة', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "المراجعة الاكلينيكية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المراجعة الاكلينيكية', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "الرعاية الصحية المنزلية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الرعاية الصحية المنزلية', Username="Medical_Services", IdOrder=IDN).save() 
            elif department == "الرعاية الصيدلية ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الرعاية الصيدلية ', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "خدمات التغذية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='خدمات التغذية', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "التغذية السريريه":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التغذية السريريه', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "الاشعة":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الاشعة', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "المختبر و نقل الدم":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المختبر و نقل الدم', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "العلاج الطبيعي ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العلاج الطبيعي ', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "التوعية الدينية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التوعية الدينية', Username="Support_Medical_Services", IdOrder=IDN).save() 
            elif department == "الجودة وسلامة المرضى":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الجودة وسلامة المرضى', Username="Quality_and_patient_safety", IdOrder=IDN).save() 
            elif department == "التواصل المؤسسي":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التواصل المؤسسي', Username="corporate_communication", IdOrder=IDN).save() 
            elif department == "الشؤون الأكاديمية و التدريب":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون الأكاديمية و التدريب', Username="Academic_Affairs_and_Training", IdOrder=IDN).save() 
            elif department == "التطوير و المشاريع ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التطوير و المشاريع ', Username="KPI", IdOrder=IDN).save() 
            elif department == "تنمية الإرادات":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='تنمية الإرادات', Username="revenue_development", IdOrder=IDN).save() 
            elif department == "الشؤون القانونية و الإلتزام":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون القانونية و الإلتزام', Username="Legal_Compliance", IdOrder=IDN).save() 
            elif department == "الادارة المناوبة":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الادارة المناوبة', Username="shift_management", IdOrder=IDN).save() 
            elif department == "تجربة المريض":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='تجربة المريض', Username="patient_experience", IdOrder=IDN).save() 
            elif department == "المستودعات الطبية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المستودعات الطبية', Username="Medical_supplies", IdOrder=IDN).save()
            elif department == "المستودعات غير الطبية ":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المستودعات غير الطبية ', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "التجهيزات":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التجهيزات', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "المشتريات":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='المشتريات', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "العقود":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='العقود', Username="Medical_supplies", IdOrder=IDN).save() 
            elif department == "الموارد البشرية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الموارد البشرية', Username="HR", IdOrder=IDN).save() 
            elif department == "الشؤون المالية":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='الشؤون المالية', Username="financial_affairs", IdOrder=IDN).save() 
            elif department == "التشغيل":
                 Doctor.objects.create(NumJob=EmployeeNumber, NameUser=fullname,
                                         Path='التشغيل', Username="Employment", IdOrder=IDN).save() 

        return render(request, 'pages/emp_form.html')

    return render(request, 'pages/emp_form.html')


def dept_log(request):
    if request.user.is_authenticated:
        return redirect('Subscriber')
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Subscriber")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "pages/dept_log.html", context={"form": form})


def dept_logout(request):
    logout(request)
    return redirect('dept_log')


def dept_confirm(request, slug, id):
    DataE = Employee_form.objects.filter(classification=slug, id=id)
    Employee_N = 0
    for x in DataE:
        Employee_N = x.Employee_Number
    statuE = request.POST.get('status3')
    NotesE = request.POST.get('notess')

    if request.method == "POST":
        if slug == 'Administrator':
            DATAE = Administrator.objects.get(Username=str(
                request.user), NumJob=Employee_N, IdOrder=id)
            DATAE.Notes = NotesE
            DATAE.State = True
            DATAE.Option_dep = statuE
            DATAE.save()

        elif slug == 'Doctor':
            DATAE = Doctor.objects.get(Username=str(
                request.user), NumJob=Employee_N, IdOrder=id)
            DATAE.Notes = NotesE
            DATAE.State = True
            DATAE.Option_dep = statuE
            DATAE.save()

        else:
            DATAE = Nursing.objects.get(Username=str(
                request.user), NumJob=Employee_N, IdOrder=id)
            DATAE.Notes = NotesE
            DATAE.State = True
            DATAE.Option_dep = statuE
            DATAE.save()

        return redirect('Subscriber')
    context = {
        'DataE': DataE,
        'name': str(request.user),
    }
    return render(request, 'pages/dept_confirm.html', context)


def dept_check(request, slug):
    form = Employee_form.objects.filter(classification=slug)
    if slug == 'Administrator':
        formstate = Administrator.objects.filter(Username=str(request.user))
    elif slug == 'Doctor':
        formstate = Doctor.objects.filter(Username=str(request.user))
    else:
        formstate = Nursing.objects.filter(Username=str(request.user))
    mylist = zip(form, formstate)
    idorder = 0
    for x in formstate:
        idorder = x.IdOrder
        break
    if slug == 'Administrator':
        formstate1 = Administrator.objects.filter()
    elif slug == 'Doctor':
        formstate1 = Doctor.objects.filter()
    else:
        formstate1 = Nursing.objects.filter()
    
    context = {
        'form': mylist,
        'check' : str(request.user) == "HR", 
        "Is_approved" : formstate1,
    }
    
    return render(request, 'pages/dept_check.html' , context)


def c_empcheck(request):
    idn = request.POST.get('num')
    if request.method == "POST":
        idn = int(idn)
        return redirect(f'/c_all/{idn}/')
    return render(request, 'pages/c_empcheck.html', {"id": idn})


def c_currentstat(request, id, slug):
    form = Employee_form.objects.get(id = id)
    if slug == 'Administrator':
        DATAE = Administrator.objects.filter(IdOrder=id)
    elif slug == 'Doctor':
        DATAE = Doctor.objects.filter(IdOrder=id)
    else:
        DATAE = Nursing.objects.filter(IdOrder=id)
    return render(request, 'pages/c_currentstat.html', {"DATAE": DATAE , "item1" :form})


def c_all(request, id):
    step1 = Employee_form.objects.filter(Employee_Number=id)
    for x in step1:
        if x.classification == 'Administrator':
            check = False
            Is_rejection = False
            DATAE = Administrator.objects.filter(IdOrder=x.id)
            for y in DATAE:
                if y.Option_dep == 'rejection':
                    Is_rejection = True
                    break
                if y.Option_dep == 'approved':
                    check = True
                else:
                    check = False
                    break
            if Is_rejection:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'rejection'
                Edit.save()
            elif check:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'approved'
                Edit.save()
            else:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'pending'
                Edit.save()
        elif x.classification == 'Doctor':
            check = False
            Is_rejection = False
            DATAE = Doctor.objects.filter(IdOrder=x.id)
            for y in DATAE:
                if y.Option_dep == 'rejection':
                    Is_rejection = True
                    break
                if y.Option_dep == 'approved':
                    check = True
                else:
                    check = False
                    break
            if Is_rejection:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'rejection'
                Edit.save()
            elif check:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'approved'
                Edit.save()
            else:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'pending'
                Edit.save()
        else:
            check = False
            Is_rejection = False
            DATAE = Nursing.objects.filter(IdOrder=x.id)
            for y in DATAE:
                if y.Option_dep == 'rejection':
                    Is_rejection = True
                    break
                else:
                    check = False
                    break
            if Is_rejection:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'rejection'
                Edit.save()
            elif check:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'approved'
                Edit.save()
            else:
                Edit = Employee_form.objects.get(id=x.id)
                Edit.FinalStat = 'pending'
                Edit.save()
    context = {
        "form": step1,
        'name': str(request.user),
    }
    return render(request, 'pages/c_all.html', context)


def Subscriber(request):
    x = str(request.user)
    return render(request, 'pages/Subscriber.html', {"x": x})
