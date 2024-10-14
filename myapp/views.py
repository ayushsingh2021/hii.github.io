from django.shortcuts import render,redirect
from . models import Employee

# Create your views here.
def index(req):
    emp=Employee.objects.all()
    empdict={"emp":emp}
    return render(req,"index.html",empdict) 
def empreg(req):
    if req.method=="POST":
        empid=req.POST["empid"]
        empname=req.POST["empname"]
        department=req.POST["department"]
        designation=req.POST["designation"]
        salary=req.POST["salary"]
        emp=Employee(empid=empid,empname=empname,department=department,designation=designation,salary=salary)
        emp.save()
        return redirect("index")

    return render(req,"empreg.html")
def delemp(req,id):
    emp=Employee.objects.get(empid=id)
    emp.delete()
    return redirect("index")
def editemp(req,id):
    emp=Employee.objects.get(empid=id)
    return render(req,"editemp.html",{"emp":emp})
def updateemp(req):
    empid=req.POST["empid"] 
    empname=req.POST["empname"]
    department=req.POST["department"]
    designation=req.POST["designation"]
    salary=req.POST["salary"]
    Employee.objects.filter(empid=empid).update(empname=empname,department=department,designation=designation,salary=salary)
    return redirect("index")
    