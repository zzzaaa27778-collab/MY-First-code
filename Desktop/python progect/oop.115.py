# ---------------------------------------------------------
# -- Object Oriented Programming => @property Decorator --
# ---------------------------------------------------------

# 1. ما هو الـ @property؟
# - هو "مُزين" (Decorator) يوضع قبل الدالة لكي يجعل بايثون تتعامل مع هذه الدالة 
#   معاملة "الخاصية العادية (Attribute)" وليست كدالة تستدعى بأقواس ().
# - يغنيك عن كتابة دوال الـ Getters الطويلة بالطريقة التقليدية، ويعطي كودك نظافة وسرعة.

# 2. القاعدة الذهبية:
# - الدالة التي يوضع فوقها `@property` تُستدعى **بدون أقواس ()** عند طباعتها أو استخدامها.
# - إذا وضعت بجانبها أقواس `()` سيظهر لك خطأ (TypeError) لأنها تحولت إلى قيمة ثابتة (Property).

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # استخدام الـ property بدلاً من دالة getter تقليدية
    @property
    def age_in_days(self):
        return self.age * 365


# --- الخلاصة ---
# - الطريقة العادية لاستدعاء دالة: obj.my_method()
# - الطريقة بعد استخدام @property: obj.my_property (بدون أقواس!)
class Member:
    def __init__(self, name, age):
        self.name = name  # Public
        self.age = age  # Public

    def say_hello(self):
        return f"Hello {self.name}"

    # هنا نستخدم الـ property لتحويل الدالة إلى خاصية تُقرأ مباشرة
    @property
    def age_in_days(self):
        return self.age * 365


# --- التجربة والتشغيل ---
one = Member("Ahmed", 40)

# 1. طباعة الخصائص العادية
print(one.name)  # النتيجة: Ahmed
print(one.age)  # النتيجة: 40

# 2. طباعة الدالة العادية (تتطلب أقواس)
print(one.say_hello())  # النتيجة: Hello Ahmed

# 3. طباعة دالة الـ @property (بدون أقواس نهائياً!)
print(one.age_in_days)  # النتيجة: 14600