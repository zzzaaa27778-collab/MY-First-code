# --------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance & MRO --
# --------------------------------------------------
# 1. Multiple Inheritance (الوراثة المتعددة):
# هي قدرة الكلاس الابن (Derived Class) على أن يرث من أكثر من كلاس أب (Base Classes) في نفس الوقت.
# الصيغة: class Derived(BaseOne, BaseTwo):
#
# 2. MRO (Method Resolution Order - ترتيب بحث الدوال):
# هو النظام الذي تتبعه لغة بايثون للبحث عن المتغيرات والدوال في الكلاسات الاباء.
# بايثون تبدأ بالبحث في الكلاس الابن نفسه، ثم تنتقل للأب الأول المكتوب بين القوسين من اليسار لليمين، ثم الأب الثاني، وهكذا.
# لمعرفة ترتيب الوراثة لأي كلاس، نستخدم الدالة: ClassName.mro()
# --------------------------------------------------
# الكلاس الأب الأول
class BaseOne:
    def __init__(self):
        print("Base One")
        
    def func_one(self):
        print("Function One From Base One")


# الكلاس الأب الثاني
class BaseTwo:
    def __init__(self):
        print("Base Two")
        
    def func_two(self):
        print("Function Two From Base Two")


# الكلاس الابن يرث من الأب الأول والأب الثاني معاً (Multiple Inheritance)[cite: 29]
class Derived(BaseOne, BaseTwo):
    pass


# ==========================================
# --- التطبيق العملي والاستدعاء ---
# ==========================================

# إنشاء كائن من الكلاس الابن
my_var = Derived()
# الناتج عند التشغيل: سيطبع "Base One" فقط، لأن بايثون تبدأ بالأب الأول حسب ترتيب الوراثة[cite: 29]

# معرفة ترتيب البحث والوراثة (MRO - Method Resolution Order)[cite: 30]
print(Derived.mro())
# الناتج: يظهر لك قائمة بترتيب الكلاسات التي تبحث فيها بايثون

# استخدام الدوال الموروثة من كلا الأبوين عبر الكائن الواحد[cite: 32]
my_var.func_one()  # موروثة من BaseOne
my_var.func_two()  # موروثة من BaseTwo