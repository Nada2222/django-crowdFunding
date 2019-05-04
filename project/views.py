from django.shortcuts import *
from .forms import *
from .models import *
from django.contrib import messages
from django.forms import modelformset_factory
import datetime

format_str = '%Y-%m-%d'
user = User.objects.get(id=1)
form_search= SearchForm()
def category(request,id):
    category = Category.object.get(id=id)
    projects = Project.objects.all().filter(category=category)
    return render(request, 'project/category.html', {"category": category,
                                                     "projects":projects,
                                                     "formsarch":form_search})




def list_cates(request):
    categories = Category.objects.all()
    categories_names = list()
    for category in categories:
        categories_names.append(category.name)
        print(category.name)
    return render(request, 'project/list_cates.html',
                  {"categories": categories,
                   "formsarch": form_search})

def showOne(request,id):
    project = Project.objects.get(id=id)
    related=[]
    try:
        tag = Tag.objects.filter(project_id=project)
        for t in tag:

            tags = Tag.objects.filter(tag=t.tag)
            for pro in tags:
                if pro.project.id==id:
                    continue
                else:

                    related.append(pro.project)
    except Tag.DoesNotExist:
        pass

    try:
        comments = Comment.objects.filter(project_id=id)
    except Comment.DoesNotExist:
        comments = None
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
        "comments": comments,
        "formsarch": form_search,
        "related":related})


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
        try :
            Project.objects.get(id=id, user=user)

            Project.objects.get(id=id).delete()
            return redirect('list_cats')

        except Project.DoesNotExist():
            pass

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
            Projectobj = formPro.save(commit=False)
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
                  {'formPro': formPro, 'formset': formset, 'form_tags': form_tags,
                   "formsarch": form_search})


def search (request):
    if request.method == 'POST':
        searched = []
        try:
            searched.append (Project.objects.get(title=request.POST['search']))
        except Project.DoesNotExist:

            try:


                tags = Tag.objects.filter(tag=request.POST['search'])


                for pro in tags:
                    searched.append(pro.project)
                print (searched)
            except Category.DoesNotExist or Project.DoesNotExist:
                searched.append ("No results")


    return render(request, 'project/search.html',{"formsarch": form_search,"searched":searched})



