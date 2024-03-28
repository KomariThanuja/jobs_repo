import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Thanujobs.settings')
import django
django.setup()

from testapp.models import Hydjobs1,Bngjobs1,Punejobs1
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','Team Engineer','HR','Associate Engineer'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hyd_jobs_record=Hydjobs1.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,email=femail,phonenumber=fphonenumber)
n=int(input("Enter number of records:"))
populate(n)
print(f'{n} Records inserted successfully........')

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','Team Engineer','HR','Associate Engineer'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        bng_jobs_record=Bngjobs1.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,email=femail,phonenumber=fphonenumber)
n=int(input("Enter number of records:"))
populate(n)
print(f'{n} Records inserted successfully........')

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','Team Engineer','HR','Associate Engineer'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        pune_jobs_record=Punejobs1.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,email=femail,phonenumber=fphonenumber)
n=int(input("Enter number of records:"))
populate(n)
print(f'{n} Records inserted successfully........')