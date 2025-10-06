from faker import Faker
import uuid
from datetime import datetime, timezone
import random

class OrgGenerator:
    organization_list = []  

    @classmethod
    def init(cls):
        fake = Faker()  
        cls.organization_list = []  

        for _ in range(5):
            now = datetime.now(timezone.utc).isoformat()
            company_name = fake.company()
            short_name = company_name.lower().replace(" ", "-")  
            domain = f"{short_name}.{fake.random_element(elements=('com', 'net', 'io', 'org'))}"

            org_data = {
                "org": {
                    "created_at": now,
                    "display_name": company_name,
                    "domain": domain,
                    "id": str(uuid.uuid4()), 
                    "short_name": short_name,
                    "status": "active",
                    "updated_at": now,
                },
                "settings": {} 
            }

            cls.organization_list.append(org_data)

    @classmethod
    def generate_org(cls):
        if not cls.organization_list:
            raise ValueError("No organizations generated. Please call 'init()' first.")
        
        return random.choice(cls.organization_list)
