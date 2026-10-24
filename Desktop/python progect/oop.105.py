# =====================================================================
# --- ملخص درس: Object Oriented Programming -> Instance Attributes & Methods ---
# =====================================================================

# [1] التعليق الأصلي:
# -- Object Oriented Programming => Instance Attributes and Methods --
# الشرح بالعربي: البرمجة كائنية التوجه - خصائص وخصائص الكائنات والدوال التابعة لها.

# [2] التعليق الأصلي:
# Self: Point To Instance Created From Class
# الشرح بالعربي: كلمة (self) تعود وتدل على الكائن (Instance) الجديد الذي يتم إنشاؤه من الـ Class.

# [3] التعليق الأصلي:
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# الشرح بالعربي: خصائص الكائن هي المتغيرات التي يتم تعريفها وبناؤها داخل دالة البناء (__init__).

# [4] التعليق الأصلي:
# Instance Methods Take Self Parameter Which Point To Instance Created From Class
# الشرح بالعربي: دوال الكائن تأخذ المعامل (self) الذي يشير إلى الكائن المُنشأ.

# [5] التعليق الأصلي:
# Instance Methods Can Have More Than One Parameter Like Any Function
# الشرح بالعربي: دوال الكائن يمكنها استقبال أكثر من باراميتر تماماً مثل أي دالة عادية في بايثون.

# [6] التعليق الأصلي:
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# الشرح بالعربي: دوال الكائن تستطيع الوصول بحرية تامة إلى الخصائص والدوال الموجودة داخل نفس الكائن.

# [7] التعليق الأصلي:
# Instance Methods Can Access The Class Itself
# الشرح بالعربي: دوال الكائن يمكنها أيضاً الوصول إلى الصنف (Class) نفسه.


# =====================================================================
# --- الأكواد الأساسية المهمة (الملخص العملي للتطبيق) ---
# =====================================================================

class Member:
    def __init__(self, first_name, middle_name, last_name):
        # تخزين الباراميترات كـ Instance Attributes خاصة بكل كائن
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

# إنشاء كائنات (Instances) مستقلة مع تمرير البيانات:
member_one = Member("Osama", "Mohamed", "Elsayed")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# طريقة طباعة واستدعاء الخصائص الخاصة بكل كائن:
print(member_one.fname)  # لطباعة الاسم الأول للكائن الأول
print(member_one.fname, member_one.mname, member_one.lname)  # لطباعة الاسم الثلاثي كاملاً