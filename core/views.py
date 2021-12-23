from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core import serializers

vehicle_types={
    1:"Private Car",
    2:"Domestic Trailers",
    3:"Caravans",
    4:"Commercial Vehicle",
    5:"Taxis",
    6:"Commercial Trailers",
    7:"Motor Cylces",
    8:"Omnibus and Commuters - Upto 30 seats",
    9:"Omnibus and Commuters - 31 t0 60 seats",
    10:"Omnibus and Commuters - More than 60 seats",
    11:"School Bus - upto 30 seats",
    12:"School Bus - 31 to 60 seats",
    13:"School Bus - More than 60 seats",
    14:"Staff Bus - Upto 30 seats",
    15:"Staff Bus - 31 to 60 seats",
    16:"Staff Bus - More than 60 seats",
    17:"Fork Lifts",
    18:"Tractors",
    19:"Tractors/Combine Harvesters",
    20:"Ambulance, Fire Engine, Hearse",
    21:"Special Type Equipment (Dozers, Graders etc)"
}  


vehicle_usage={
    1:"Social Domestic and Personal Use",
    2:"Business Use",
    3:"Fleet",
    4:"Private Hire (Car Hire)",
    5:"Driving School",
    6:"Trailers",
    7:"Caravans",
    8:"Own Use",
    9:"Hire And Reward",
    10:"Fleet Own Use",
    11:"Fleet Hire And Reward",
    12:"Public Hire",
    13:"Agriculture",
    14:"Commuter Omnibus",
    15:"School Bus",
    16:"Staff Bus",
    17:"Social Domestic and Personal Reward",
    19:"Hire",
    20:"Implements",
    21:"Contractors Plant And Hire"
}


#quote end point 
def get_quote(request):
    if request.method == 'GET':
        sum_insured=float(request.GET.get('sum_insured'))
        vehicle_type=int(request.GET.get('vehicle_type'))
        use_case=int(request.GET.get('use_case')) 
        try:    
            p = PackageRate.objects.get(use_case__vehicle__vehicle_type=vehicle_types[vehicle_type], use_case__use_case=vehicle_usage[use_case])
            def get_package_details(rate,minmum_si):
                premiumValue=(rate)*minmum_si
                stamp_duty=premiumValue*.05
                gvt_lvy=premiumValue*0.12
                total=premiumValue+stamp_duty+gvt_lvy
                return {
                "premium" : round(premiumValue,2),
                "stamp_duty":round(stamp_duty,2),
                "gtv_lvy":round(gvt_lvy,2),
                "total_anual_premium":round(total,2),
                }
            std_rate = p.standard_package_rate
            premium_rate = p.premimum_package_rate
            ultra_rate = p.ultra_package_rate          
            data = {
                'standard_package':get_package_details(std_rate, sum_insured),
                'premium_package':get_package_details(premium_rate, sum_insured),
                'ultra_package':get_package_details(ultra_rate, sum_insured)
                }        
            return JsonResponse(data, safe=False)
        except PackageRate.DoesNotExist:
            return JsonResponse({'error':f'Does Not Exists,for combination {vehicle_type}:{vehicle_types[vehicle_type]} vehicle type and {use_case}:{vehicle_usage[use_case]} vehicle usage'}, status=404)
        except KeyError:
            return JsonResponse({'error':f'The keys are not in range'})
            
        
        
        
    