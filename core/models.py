from django.db import models 

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=250, blank=False, null=False)
    
    def __str__(self):
        return self.vehicle_type
    

    

class UseCase(models.Model):
    use_case = models.CharField(max_length=250, blank=False, null=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.use_case}-{self.vehicle.vehicle_type}"

    
    

class PackageRate(models.Model):
    use_case = models.ForeignKey('UseCase', on_delete=models.PROTECT, null=False , blank=False)
    standard_package_rate = models.FloatField(blank=False, null=False)
    premimum_package_rate = models.FloatField(blank=False, null=False)
    ultra_package_rate = models.FloatField(blank=True, null=False)

    def __str__(self):
        return str(self.use_case)+'-'+str(self.use_case.vehicle.vehicle_type)
        
    
     
        