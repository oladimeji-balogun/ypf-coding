import faker

faker = faker.Faker()

fake_name = faker.name()

# fake_names = [
#     faker.name() for i in range(20)
# ]

fake_addresses = [
    faker.address() for i in range(20)
]

for i in fake_addresses: 
    print(i)


