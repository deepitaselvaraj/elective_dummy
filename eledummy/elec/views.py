from django.shortcuts import render,redirect
from elec.forms import UserForm, CourseForm, UpdateForm
from elec.models import Student,Department,Course
from django.forms import ModelChoiceField
# Create your views here.
def home(request):
    UserForm.base_fields['department'] = ModelChoiceField(queryset=Department.objects.all())
    form=UserForm()
    print("get or post")
    print(form.errors)
    if request.method=="POST":
        print("post")
        form=UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            temp=form.save(commit=False)
            request.session['uname']=temp.user
            request.session['dept']=temp.department
            temp.save()
            return redirect('choose_course')
    return render(request, 'first.html', {'form':form})









def choose_course(request):
    chooser=(request.session['uname']).lower()
    cdept=request.session['dept']
    eligible=[]

    #computer technology
    if cdept=='Computer Technology':
        print(eligible)
        courses=Course.objects.all()
        for course in courses:
            if course.course_name=='Parallel Computing':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<15):
                    eligible.append(course)

            elif course.course_name=='TCP/IP':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<14):
                    eligible.append(course)

            elif (course.course_name=='Cyber Forensics') or (course.course_name=='Parallel and Distributed Computing') :
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='Internet Of Things':
                pass

            elif course.course_name=='Advanced Database Technologies':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)


    #information technology
    elif cdept=='Information Technology':
        print(eligible)
        courses=Course.objects.all()
        for course in courses:
            if course.course_name=='Parallel Computing':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='TCP/IP':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif (course.course_name=='Cyber Forensics') or (course.course_name=='Parallel and Distributed Computing') :
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='Internet Of Things':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='Advanced Database Technologies':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<9):
                    eligible.append(course)

    #data analytics
    elif cdept=='Data Analytics':
        courses=Course.objects.all()
        for course in courses:
            if course.course_name=='Parallel Computing':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<4):
                    print("less than 4")
                    eligible.append(course)

            elif course.course_name=='TCP/IP':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif (course.course_name=='Cyber Forensics') or (course.course_name=='Parallel and Distributed Computing') :
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='Internet Of Things':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<11):
                    eligible.append(course)

            elif course.course_name=='Advanced Database Technologies':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<9):
                    eligible.append(course)
        print(eligible)

    
    #computer applications
    elif cdept=='Computer Applications':
        courses=Course.objects.all()
        for course in courses:
            if course.course_name=='Parallel Computing':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='TCP/IP':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<5):
                    eligible.append(course)

            elif (course.course_name=='Cyber Forensics') or (course.course_name=='Parallel and Distributed Computing') :
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)

            elif course.course_name=='Internet Of Things':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<11):
                    eligible.append(course)

            elif course.course_name=='Advanced Database Technologies':
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<9):
                    eligible.append(course)

    #computer science A and B
    elif cdept=='Computer Science A' or cdept=='Computer Science B':
        print(eligible)
        courses=Course.objects.all()
        for course in courses:
                if(Student.objects.filter(department=cdept,course_alloted=course).count()<10):
                    eligible.append(course)
                    
    print(eligible)

    CourseForm.base_fields['course_chosen'] = ModelChoiceField(queryset=Course.objects.filter(course_name__in=eligible ))

    form=CourseForm()
    print("get or post")
    if request.method=="POST":
        print("post")
        form=CourseForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("valid")
            temp=form.save(commit=False)
            print(temp.course_chosen)
            Student.objects.filter(user=chooser).update(course_chosen=temp.course_chosen, course_alloted=temp.course_chosen)
            print(temp.course_alloted)
            filled=Student.objects.filter(course_alloted=temp.course_chosen).count()
            dept=Department.objects.get(course_offered=temp.course_chosen)
            vacant=dept.strength-filled
            Course.objects.filter(course_name=temp.course_chosen).update(filled_seats=filled, vacancy=vacant)
            return redirect('course_allotment')
    return render(request, 'choose_course.html', {'form':form})









def course_allotment(request):
    uname=request.session['uname']
    student=Student.objects.get(user=uname)
    stu=student.course_chosen
    return render(request,'allotment.html',{'student':student})







def first_page(request):
    return render(request,'first_page.html')





def display_profile(request):
    uname=request.session['uname']
    student=Student.objects.get(user=uname)
    return render(request,'display_profile.html',{'student':student})






def update_profile(request):
    uname=request.session['uname']
    student_id=Student.objects.get(user=uname)
    form=UpdateForm(request.POST or None, instance=student_id)
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect('display_profile')
    return render(request, 'update_profile.html',{'form':form})

