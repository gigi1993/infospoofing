from django.shortcuts import render
from django.utils import timezone
#from website.models import Visit
# import pyasn
# from geolite2 import geolite2

# Create your views here.

# Function that get user's IP
# def get_ip(request):
# 	try:
# 		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
# 		if x_forward:
# 			ip = x_forward.split(",")[0]
# 		else:
# 			ip = request.META.get("REMOTE_ADDR")
# 	except:
# 		ip = ""
# 	return ip

# # Function that lookup the AS given the IP
# def get_asn(ip):
#     asndb = pyasn.pyasn('/home/infospoofing/crowdsourcing_experiment/ipasn.dat')        # Initialize database ASN
#     asn = asndb.lookup(ip)[0]
#     return asn

# # Function that return the country code given the IP
# def get_country_code(ip):
#     reader = geolite2.reader()              # get the Country code using GeoLite2
#     result = reader.get(ip)                 # create a dictionary with different fields ({city}, {country}...)
#     geolite2.close()
#     code=result['country']['iso_code']      #lookup
#     return code


def home(request):
    return render(request, 'website/home.html', {})
def about(request):
    return render(request, 'website/about.html', {})

def UK(request):
    # current_IP = get_ip(request)                            # Get user's IP
    # current_ASN = get_asn(current_IP)               # Get user's ASN
    current_ASN = "174"
    # current_country = get_country_code(current_IP)          # Get user's country
    # AutonomousSystem.objects.create(date = timezone.now(), ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/UK/UK.html', {'current_ASN': current_ASN})
def UK_pie(request):
    return render(request, 'website/UK/UK_pie.html', {})
def UK_AS(request):
    return render(request, 'website/UK/UK_AS.html', {})
def UK_table(request):
    return render(request, 'website/UK/UK_table.html', {})

def DE(request):
    # current_IP = get_ip(request)                            # Get user's IP
    # current_ASN = get_asn(current_IP)               # Get user's ASN
    current_ASN = "174"
    # current_country = get_country_code(current_IP)          # Get user's country
    # AutonomousSystem.objects.create(date = timezone.now(), ip_address = current_IP, asn=current_ASN, country=current_country)
    return render(request, 'website/DE/DE.html', {'current_ASN': current_ASN})
def DE_pie(request):
    return render(request, 'website/DE/DE_pie.html', {})
def DE_AS(request):
    return render(request, 'website/DE/DE_AS.html', {})
def DE_table(request):
    return render(request, 'website/DE/DE_table.html', {})