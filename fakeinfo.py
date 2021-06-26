from faker import Faker
fake = Faker()
print("some anonymus name:-"+fake.name())
print("some anonymus mail ID:-"+fake.email())
print("country:-"+fake.country())

print(fake.profile())                                                        
