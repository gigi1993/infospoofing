from django.shortcuts import render
from django.utils import timezone
from website.models import Visit
#import pyasn
#from geolite2 import geolite2

# Create your views here.

#Function that get user's IP
def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

# Function that lookup the AS given the IP
#def get_asn(ip):
#    asndb = pyasn.pyasn('/home/gigi1993/infospoofing/ipasn.dat')        # Initialize database ASN
#    asn = asndb.lookup(ip)[0]
#    return asn

# # Function that return the country code given the IP
# def get_country_code(ip):
#     reader = geolite2.reader()              # get the Country code using GeoLite2
#     result = reader.get(ip)                 # create a dictionary with different fields ({city}, {country}...)
#     geolite2.close()
#     code=result['country']['iso_code']      #lookup
#     return code


def home(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Home", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/home.html', {})
def remediation(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Remediation", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/remediation.html', {})
def about(request):
    return render(request, 'website/about.html', {})

def AU(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Australia", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/AU/AU.html', {'current_ASN': current_ASN})
def AU_pie(request):
    return render(request, 'website/AU/AU_pie.html', {})
def AU_AS(request):
    return render(request, 'website/AU/AU_AS.html', {})
def AU_table(request):
    return render(request, 'website/AU/AU_table.html', {})

def DE(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Germany", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/DE/DE.html', {'current_ASN': current_ASN})
def DE_pie(request):
    return render(request, 'website/DE/DE_pie.html', {})
def DE_AS(request):
    return render(request, 'website/DE/DE_AS.html', {})
def DE_table(request):
    return render(request, 'website/DE/DE_table.html', {})

def IT(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Italy", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/IT/IT.html', {'current_ASN': current_ASN})
def IT_pie(request):
    return render(request, 'website/IT/IT_pie.html', {})
def IT_AS(request):
    return render(request, 'website/IT/IT_AS.html', {})
def IT_table(request):
    return render(request, 'website/IT/IT_table.html', {})

def NL(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Netherlands", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/NL/NL.html', {'current_ASN': current_ASN})
def NL_pie(request):
    return render(request, 'website/NL/NL_pie.html', {})
def NL_AS(request):
    return render(request, 'website/NL/NL_AS.html', {})
def NL_table(request):
    return render(request, 'website/NL/NL_table.html', {})

def PL(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "Poland", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/PL/PL.html', {'current_ASN': current_ASN})
def PL_pie(request):
    return render(request, 'website/PL/PL_pie.html', {})
def PL_AS(request):
    return render(request, 'website/PL/PL_AS.html', {})
def PL_table(request):
    return render(request, 'website/PL/PL_table.html', {})

def UK(request):
#   current_IP = get_ip(request)                    # Get user's IP
#   current_ASN = get_asn(current_IP)               # Get user's ASN
#   current_country = get_country_code(current_IP)  # Get user's country
    current_IP = "A.B.C.D"
    current_ASN = "Y"
    current_country = "X"
    Visit.objects.create(date = timezone.now(), visited = "United Kingdom", ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/UK/UK.html', {'current_ASN': current_ASN})
def UK_pie(request):
    return render(request, 'website/UK/UK_pie.html', {})
def UK_AS(request):
    return render(request, 'website/UK/UK_AS.html', {})
def UK_table(request):
    return render(request, 'website/UK/UK_table.html', {})