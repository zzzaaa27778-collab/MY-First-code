# --------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# --------------------------------------------------

# الفكرة الأساسية:
# بدلاً من استخدام التخفي (Name Mangling) للوصول للبيانات الخاصة (Private)،
# نستخدم الطرق البرمجية الصحيحة المعتمدة وهي الـ Getters والـ Setters.

class Member:
    def __init__(self, name):
        self.__name = name  # متغير خاص (Private) لا يُرى من الخارج

    # 1. الـ Getter (جالب القيمة):
    # دالة تعيد قيمة المتغير الخاص لقراءتها فقط من الخارج
    def get_name(self):
        return self.__name

    # 2. الـ Setter (مُعدّل القيمة):
    # دالة تستقبل قيمة جديدة لتعديل المتغير الخاص بأمان
    def set_name(self, new_name):
        self.__name = new_name


# --- ملخص المفهوم ---
# - get_name(): نستخدمها للطباعة أو العرض (قراءة فقط).
# - set_name('New Value'): نستخدمها لتغيير الاسم القديم باسم جديد.
class Member:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


# --- تجربة الكود ---

# 1. إنشاء الكائن بالاسم الأول
one = Member("Ahmed")

# 2. قراءة الاسم باستخدام الـ Getter وطباعته
print(one.get_name())  # المتوقع في التيرمنال: Ahmed

# 3. تعديل الاسم باستخدام الـ Setter إلى اسم جديد
one.set_name("Abbas")

# 4. قراءة الاسم مجدداً بعد التعديل للتأكد
print(one.get_name())  # المتوقع في التيرمنال: Abbas