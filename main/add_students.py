from main.models import Student, Group
from django.core.files import File

# Guruh yaratish yoki olish
group, _ = Group.objects.get_or_create(name="Group C")

# Default rasm yo‘li
default_image_path = "main/profile_default.avif"  # Skript bilan bir papkada bo‘lishi kerak

students_data = [
    ("Sardor", "Bekmurodov", "2004-03-05", "Erkak", "CA1234567", "sardor.bekmurodov@example.com", "+998901112301", "To'lov kontrakt asosida"),
    ("Madina", "Islomova", "2004-09-11", "Ayol", "CB9876543", "madina.islomova@example.com", "+998901112302", "Davlat granti asosida"),
    ("Botir", "Qayumov", "2004-06-18", "Erkak", "CC1928374", "botir.qayumov@example.com", "+998901112303", "To'lov kontrakt asosida"),
    ("Dilnoza", "Maxmudova", "2004-07-25", "Ayol", "CD8374652", "dilnoza.maxmudova@example.com", "+998901112304", "To'lov kontrakt asosida"),
    ("Rustam", "Aliqulov", "2003-10-14", "Erkak", "CE5647382", "rustam.aliqulov@example.com", "+998901112305", "Davlat granti asosida"),
    ("Abbos", "Xasanov", "2004-05-30", "Erkak", "CF2837465", "abbos.xasanov@example.com", "+998901112306", "To'lov kontrakt asosida"),
    ("Oysara", "Habibullayeva", "2004-02-19", "Ayol", "CG9182736", "oysara.habibullayeva@example.com", "+998901112307", "To'lov kontrakt asosida"),
    ("Javohir", "Sattorov", "2004-08-06", "Erkak", "CH3748291", "javohir.sattorov@example.com", "+998901112308", "To'lov kontrakt asosida"),
    ("Shahnoza", "Ortiqova", "2004-11-23", "Ayol", "CI6574839", "shahnoza.ortiqova@example.com", "+998901112309", "Davlat granti asosida"),
    ("Xusan", "Olimjonov", "2004-04-01", "Erkak", "CJ5463728", "xusan.olimjonov@example.com", "+998901112310", "To'lov kontrakt asosida"),
    ("Sherzod", "Murodov", "2004-12-29", "Erkak", "CK4738291", "sherzod.murodov@example.com", "+998901112311", "To'lov kontrakt asosida"),
    ("Malohat", "Raxmatova", "2004-01-09", "Ayol", "CL2837465", "malohat.raxmatova@example.com", "+998901112312", "To'lov kontrakt asosida"),
    ("Anvar", "Qurbonov", "2003-07-27", "Erkak", "CM1928374", "anvar.qurbonov@example.com", "+998901112313", "To'lov kontrakt asosida"),
    ("Shavkat", "Mamatov", "2004-05-22", "Erkak", "CN9182736", "shavkat.mamatov@example.com", "+998901112314", "Davlat granti asosida"),
    ("Habib", "Tursunov", "2004-10-04", "Erkak", "CO5647382", "habib.tursunov@example.com", "+998901112315", "To'lov kontrakt asosida"),
    ("Maftuna", "Sodiqova", "2004-03-15", "Ayol", "CP3748291", "maftuna.sodiqova@example.com", "+998901112316", "To'lov kontrakt asosida"),
    ("Murod", "Qobilov", "2004-06-20", "Erkak", "CQ6574839", "murod.qobilov@example.com", "+998901112317", "To'lov kontrakt asosida"),
    ("Shahzoda", "Sayfullayeva", "2004-09-02", "Ayol", "CR5463728", "shahzoda.sayfullayeva@example.com", "+998901112318", "Davlat granti asosida"),
    ("Jasurbek", "Tolibov", "2004-11-18", "Erkak", "CS4738291", "jasurbek.tolibov@example.com", "+998901112319", "To'lov kontrakt asosida"),
    ("Samandar", "Yoqubov", "2004-08-12", "Erkak", "CT2837465", "samandar.yoqubov@example.com", "+998901112320", "To'lov kontrakt asosida"),
]



for first_name, last_name, birth_date, gender, pasport, email, phone, edu_type in students_data:
    student = Student(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        gender=gender,
        pasport=pasport,
        email=email,
        phone=phone,
        edu_type=edu_type,
        password="111",  # Default parol
        group=group
    )
    # Har bir student uchun faylni qaytadan ochish
    with open(default_image_path, "rb") as f:
        student.image.save(f"{first_name.lower()}_{last_name.lower()}.avif", File(f), save=False)
    student.save()

print(f"{len(students_data)} ta student bir xil rasm bilan qo‘shildi ✅")
