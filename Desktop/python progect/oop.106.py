# =====================================================================
# --- ملخص درس: OOP -> Instance Methods (الدوال التابعة للكائن) ---
# =====================================================================

# [1] التعليق الأصلي:
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# الشرح بالعربي: دوال الكائن تأخذ دائماً معامل أساسي يسمى (self) والذي يشير إلى الكائن المُنشأ حالياً من الصنف.

# [2] التعليق الأصلي:
# Instance Methods Can Have More Than One Parameter Like Any Function
# الشرح بالعربي: دوال الكائن يمكنها استقبال عدة باراميترات إضافية تماماً مثل أي دالة عادية في بايثون.

# [3] التعليق الأصلي:
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# الشرح بالعربي: دوال الكائن تستطيع الوصول بحرية تامة إلى جميع خصائص (Attributes) ودوال (Methods) الكائن نفسه.

# [4] التعليق الأصلي:
# Instance Methods Can Access The Class Itself
# الشرح بالعربي: دوال الكائن قادرة أيضاً على استدعاء وتجاوز البيانات والوصول إلى الصنف (Class) نفسه.

# =====================================================================
# --- الأكواد الأساسية والتطبيق العملي لدرس 106 ---
# =====================================================================

class Member:
    def __init__(self, first_name, middle_name, last_name, gender):
        # تخزين الخصائص الخاصة بالكائن (Instance Attributes)
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

    # 1. دالة لدمج الاسم الثلاثي
    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"

    # 2. دالة لإضافة لقب حسب الجنس (ذكر / أنثى) باستخدام الشرط (if)
    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname}"
        elif self.gender == "Female":
            return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"

    # 3. دالة متقدمة تستدعي دوال أخرى من نفس الكائن
    def get_all_info(self):
        # استدعاء دالة name_with_title ودالة full_name داخل نفس الكائن
        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

# إنشاء الكائنات مع تمرير البيانات (الاسم الثلاثي والجنس):
member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# طريقة الاستدعاء وطباعة النتائج:
print(member_one.full_name())        # يطبع الاسم كاملاً
print(member_one.name_with_title())  # يطبع الاسم مع اللقب حسب الجنس
print(member_one.get_all_info())     # يطبع التقرير الشامل المستدعى من الدوال الداخلية