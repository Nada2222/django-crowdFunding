from django.shortcuts import *
from .forms import *
from .models import *
from django.contrib import messages
from django.forms import modelformset_factory
import datetime
<<<<<<< HEAD
=======
import operator
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d

format_str = '%Y-%m-%d'
user = User.objects.get(id=1)

<<<<<<< HEAD
=======
def avg_rate(id):
    mkm = 1
    total_rate = 0
    rates = Rate.objects.all().filter(project=id)
    for rate in rates:
        total_rate = (total_rate + rate.rate)
    if len(rates) == 0:
        total_rate = total_rate / mkm
    else:
        total_rate = total_rate / len(rates)
    return total_rate


def home(request):
    projects_avg_rate = {}
    projects_avg_rate2 = {}
    highly_rated = []
    key = []
    value = []
    projects = Project.objects.all()
    for project in projects:
        key.append(project.id)
        value.append(avg_rate(project.id))
    projects_avg_rate = dict(zip(key, value))
    print(projects_avg_rate)
    print("data")
    # to sort the dict by value
    sorted_d = sorted(projects_avg_rate.items(), key=operator.itemgetter(0))
    # to convert the list of tuple into dict
    for a, b in sorted_d:
        projects_avg_rate2.setdefault(a, b)
    print(projects_avg_rate2)
    print(sorted_d)
    for i in projects_avg_rate.keys():
        highly_rated.append(Images.objects.all().filter(project=i)[0])
    for i in highly_rated:
        print(i.image)
    print(highly_rated)
    print("highly_rated")



    latest_projects = Project.objects.all().order_by('-start_date')
    featured_projects = Project.objects.all().filter(featured=True).order_by('-start_date')
    # print(featured_projects[0].title)
    rate = Rate.objects.all().filter(project=1)
    print("rate")
    # print(rate[0])
    return render(request, 'project/home.html', {"featured_projects": featured_projects, "latest_projects":latest_projects, "highly_rated":highly_rated})

def category(request,id):
    category = Category.object.get(id=id)
    projects = Project.objects.all().filter(category=category)
    return render(request, 'project/category.html', {"category": category, "projects":projects})

def list_cates(request):
    categories = Category.objects.all()
    categories_names = list()
    for category in categories:
        categories_names.append(category.name)
        print(category.name)
    return render(request, 'project/list_cates.html', {"categories": categories})


>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
def category(request,id):
    category = Category.object.get(id=id)
    projects = Project.objects.all().filter(category=category)
    return render(request, 'project/category.html', {"category": category, "projects":projects})




def list_cates(request):
    categories = Category.objects.all()
    categories_names = list()
    for category in categories:
        categories_names.append(category.name)
        print(category.name)
    return render(request, 'project/list_cates.html', {"categories": categories})

def showOne(request,id):
<<<<<<< HEAD
=======
    img = Images.objects.all().filter(id=id)
    print(img[0].image)
    print ("ggggggggggggg")
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
    try:
        comments = Comment.objects.filter(project_id=id)
    except Comment.DoesNotExist:
        comments = None
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        comment = Form_comment(request.POST)
        donation = Form_donation(request.POST)
        report_pro = Form_reportProject()
        report_com = Form_reportComment()
        if comment.is_valid():
            print("valid")
            print(type(id))
            print(request.POST['text'])

        comment_obj = Comment()
        comment_obj.user = user				
        comment_obj.project_id = id





        comment_obj.text = request.POST['text']
        comment_obj.save()


    else:


        comment = Form_comment()
        donation = Form_donation()
        report_pro = Form_reportProject()
        report_com = Form_reportComment()



    return render(request, 'project/showOne.html', {
        "project": project,
        "form1": comment,
        "form2": donation,
        "form3":report_pro,
        "form4": report_com,
<<<<<<< HEAD
        "comments": comments})
=======
        "comments": comments,
        "img": img})
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d


def addDonate(request,id):
    if request.method == 'POST':
        donation = Form_donation(request.POST)
        totaltarget = Project.objects.values_list('total_target').get(id=id)[0]
        print(totaltarget)
        print('inside donation')
        if donation.is_valid():
            if int(request.POST['donation']) + calcDontion(id) < totaltarget:

                donation_obj = Donation()
                donation_obj.user = user
                donation_obj.project_id = id
                donation_obj.donation = request.POST['donation']
                donation_obj.save()
            else:
                messages.error(request, 'By this donation Project  will overlap the total target')
            return redirect('show_project', id=id)


def report_pro(request,id):
    if request.method == 'POST':
        report_pro = Form_reportProject(request.POST)
        if report_pro.is_valid():
            report_pro_obj = Report_project()
            report_pro_obj.user= user
            report_pro_obj.project_id = id
            report_pro_obj.text = request.POST['text']
            report_pro_obj.save()

        return redirect('show_project', id=id)

def report_com(request,id):
    print("inside report comment")
    if request.method == 'POST':
        report_com = Form_reportComment(request.POST)
        if report_com.is_valid():
            report_com_obj = Report_comment()
            report_com_obj.user = user
            report_com_obj.project_id = id
            report_com_obj.text = request.POST['text']
            report_com_obj.comment_id = request.POST['comId']
            report_com_obj.save()

        return redirect('show_project', id=id)
def cancel_pro(request,id):
    totaltarget = Project.objects.values_list('total_target').get(id=id)[0]

    if calcDontion(id) < totaltarget/4:
        Project.objects.get(id=id).delete()
    #handling redirect to userhome

def calcDontion(id):
    sum=0
    donations=Donation.objects.values_list('donation').filter(project_id=id)
    try:
       for i in donations:
           sum=sum+int(i[0])
       return sum
    except Comment.DoesNotExist:
       return 0
def new(request):


    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm)
    if request.method == 'POST':
        Projectobj = Project()
        formPro =Form_Project(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        form_tags = TagForm(request.POST)
        print(formset)
        if formPro.is_valid() and formset.is_valid() and form_tags.is_valid():
<<<<<<< HEAD
            Projectobj = formPro.save(commit=False)
=======
            ###################################################
            print (type(int(request.POST['category'])))
            # category=Category.objects.filter(name=request.POST['category'])
            print (request.POST['end_date'])
########################################################################################3

            Projectobj.title=request.POST['title']
            Projectobj.details=request.POST['details']
            Projectobj.total_target=request.POST['total_target']
            formPro.category_id =int(request.POST['category'])
            formPro.start_date = request.POST['start_date']
            formPro.end_date = request.POST['end_date']
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
            Projectobj.user= user
            Projectobj.save()
            tags_Sent = request.POST['tag']
            tags = tags_Sent.split()
            print (tags)

            for tag in tags:
                tag_obj = Tag()
                tag_obj.tag = tag
                tag_obj.project= Projectobj
                tag_obj.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    print (image)
                    if image != None:

                        photo = Images()
                        photo.image=image
                        photo.project= Projectobj
                        photo.save()


            return redirect('show_project', id=Projectobj.id)

        else:
            print(formPro.errors, formset.errors)
    else:
        formPro = Form_Project()
        formset = ImageFormSet()
        form_tags= TagForm()
    return render(request, 'project/new.html',
                  {'formPro': formPro, 'formset': formset, 'form_tags': form_tags})


    pass
