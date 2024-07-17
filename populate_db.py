import random
from datetime import datetime, timedelta
from faker import Faker
from app import create_app, db
from app.models import Farmer, Worker, Cattle, Feed, Medicine, Equipment, MilkProduction, MilkSales, MaintenanceCosts

fake = Faker()

def populate_db():
    app = create_app()
    app.app_context().push()

    db.drop_all()
    db.create_all()

    # Create Farmers
    farmers = []
    for _ in range(5):
        farmer = Farmer(name=fake.name())
        db.session.add(farmer)
        farmers.append(farmer)

    db.session.commit()
    print(f"Committed {len(farmers)} farmers.")

    # Create Workers
    for farmer in farmers:
        for _ in range(random.randint(1, 5)):
            worker = Worker(farmer_id=farmer.id, name=fake.name())
            db.session.add(worker)

    db.session.commit()
    num_workers = Worker.query.count()
    print(f"Committed {num_workers} workers.")

    # Create Cattle
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            cattle = Cattle(
                farmer_id=farmer.id,
                status=random.choice(['pregnant', 'weaning', 'sick', 'producing milk']),
                loss=random.uniform(0, 1000)
            )
            db.session.add(cattle)

    db.session.commit()
    num_cattle = Cattle.query.count()
    print(f"Committed {num_cattle} cattle.")

    # Create Feed
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            feed = Feed(
                farmer_id=farmer.id,
                cost=random.uniform(100, 500),
                quantity=random.uniform(10, 50)
            )
            db.session.add(feed)

    db.session.commit()
    num_feed = Feed.query.count()
    print(f"Committed {num_feed} feed records.")

    # Create Medicine
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            medicine = Medicine(
                farmer_id=farmer.id,
                cost=random.uniform(100, 500),
                quantity=random.uniform(10, 50)
            )
            db.session.add(medicine)

    db.session.commit()
    num_medicine = Medicine.query.count()
    print(f"Committed {num_medicine} medicine records.")

    # Create Equipment
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            equipment = Equipment(
                farmer_id=farmer.id,
                cost=random.uniform(100, 500),
                quantity=random.uniform(10, 50)
            )
            db.session.add(equipment)

    db.session.commit()
    num_equipment = Equipment.query.count()
    print(f"Committed {num_equipment} equipment records.")

    # Create MilkProduction
    current_date = datetime.now().date()
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            milk_production = MilkProduction(
                farmer_id=farmer.id,
                date=current_date,
                milk_produced=random.uniform(500, 2000),
                quantity=random.uniform(100, 500),
                price=random.uniform(20, 50)
            )
            db.session.add(milk_production)
            current_date += timedelta(days=1)

    db.session.commit()
    num_milk_production = MilkProduction.query.count()
    print(f"Committed {num_milk_production} milk production records.")

    # Create MilkSales
    current_date = datetime.now().date()
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            milk_sales = MilkSales(
                farmer_id=farmer.id,
                date=current_date,
                revenue=random.uniform(1000, 5000),
                quantity=random.uniform(100, 500)
            )
            db.session.add(milk_sales)
            current_date += timedelta(days=1)

    db.session.commit()
    num_milk_sales = MilkSales.query.count()
    print(f"Committed {num_milk_sales} milk sales records.")

    # Create MaintenanceCosts
    current_date = datetime.now().date()
    for farmer in farmers:
        for _ in range(random.randint(10, 50)):
            maintenance_costs = MaintenanceCosts(
                farmer_id=farmer.id,
                date=current_date,
                cost=random.uniform(100, 1000)
            )
            db.session.add(maintenance_costs)
            current_date += timedelta(days=1)

    db.session.commit()
    num_maintenance_costs = MaintenanceCosts.query.count()
    print(f"Committed {num_maintenance_costs} maintenance costs records.")

    print("Database populated with random data!")

if __name__ == '__main__':
    populate_db()
