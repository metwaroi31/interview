from models import Car
from threading import Thread

toyota = Car(wheels=4, doors=4, seats=7, maxSpeed=120)
car1_thread = Thread(target=toyota.run)

BMW = Car(wheels=4, doors=4, seats=2, maxSpeed=200)
car2_thread = Thread(target=BMW.run)

car1_thread.start()
car2_thread.start()