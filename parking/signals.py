from django.db.models.signals import post_save
from django.dispatch import receiver

from parking.models import ParkingRecord

@receiver(post_save, sender=ParkingRecord)
def update_parking_spot_status(sender, instance, created, **kwargs):
    parking_spot = instance.parking_spot # Obtém a vaga de estacionamento associada ao registro
    parking_spot.is_occupied = instance.exit_time is None # Se exit_time for None, a vaga está ocupada
    parking_spot.save() # Atualiza o status da vaga de estacionamento
