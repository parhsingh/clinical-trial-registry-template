from userauth.models import PrimaryRegistry, SecondaryRegistry
import csv

def run():
    with open('scripts/data/registries.csv', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)

        existing_names = set()
        # Get existing names from both PrimaryRegistry and SecondaryRegistry
        existing_names.update(PrimaryRegistry.objects.values_list('name', flat=True))
        existing_names.update(SecondaryRegistry.objects.values_list('name', flat=True))

        for row_num, row in enumerate(reader, start=1):
            try:
                name = f"{row['name']}, {row['state']}" if row["state"] else row['name']

                if name in existing_names:
                    # Skip records that already exist in the database (name-based check)
                    print(f"Skipped data for {name} as it already exists in the database.")
                    continue

                primary_registry, _ = PrimaryRegistry.objects.get_or_create(
                    name=name,
                    defaults={
                        'type': row['type'],
                        'phone': row['phone'],
                        'district': row['district'],
                        'city': row['city'],
                        'state': row['state'],
                        'country': row['country'],
                        'pincode': row['pincode'],
                        'address': row['address']
                    }
                )

                secondary_registry, _ = SecondaryRegistry.objects.get_or_create(
                    name=name,
                    defaults={
                        'type': row['type'],
                        'phone': row['phone'],
                        'district': row['district'],
                        'city': row['city'],
                        'state': row['state'],
                        'country': row['country'],
                        'pincode': row['pincode'],
                        'address': row['address']
                    }
                )

                print(f"Imported data for {name}")

            except UnicodeDecodeError as e:
                print(f"Skipping row {row_num}: UnicodeDecodeError occurred - {e}")
                continue

            except Exception as e:
                print(f"Skipping row {row_num}: An error occurred - {e}")
                continue