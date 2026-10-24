# ----------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# ----------------------------------------------------

# 1. ما هو التغليف (Encapsulation)؟
# هو تقييد الوصول إلى البيانات (Attributes) والدوال (Methods) داخل الكلاس، 
# لحمايتها من التعديل العشوائي أو الخطأ من خارج الكلاس.

# 2. مستويات الوصول (Access Modifiers):

# أ) Public (عام):
# - كل المتغيرات والدوال التي كتبناها سابقاً كانت عامة.
# - يمكن الوصول إليها وتعديلها من أي مكان (داخل الكلاس أو خارجه).
# - مثال: self.name

# ب) Protected (محمي):
# - يتم الوصول إليه من داخل الكلاس والكلاسات الوارثة (Sub Classes فقط).
# - يُكتب مسبوقاً بشرطة سفليّة واحدة (One Underscore _).
# - مثال: self._name (بايثون تسمح بتعديله من الخارج، لكنه تحذير للمبرمج ألا يلمسه).

# ج) Private (خاص):
# - لا يمكن الوصول إليه أو تعديله إلا من داخل الكلاس نفسه فقط!
# - يُكتب مسبوقاً بشرطتين سفليتين (Two Underscores __).
# - مثال: self.__name
# - ملاحظة هامة: إذا حاولنا الوصول إليه من خارج الكلاس مباشرة سيظهر خطأ (AttributeError)،
#   ولكن بايثون تقوم بآلية تخفي اسمها الحقيقي (Name Mangling) ليصبح _ClassName__variableName 
#   (رغم أن هذا غير مستحب برمجياً إلا للضرورة القصوى).
class Member:
    def __init__(self, name):
        # self.name = name          # 1. Public (عام)
        # self._name = name         # 2. Protected (محمي بشحطة واحدة)
        self.__name = name          # 3. Private (خاص بشحطتين)

    def say_hello(self):
        return f"Hello {self.__name}" # يمكن الوصول للخاص من داخل الكلاس حصراً

# التجربة العملية:
one = Member("Ahmed")

# محاولة طباعة أو تعديل الـ Private مباشرة من الخارج ستعطي خطأ:
# print(one.__name)  -> خطأ! AttributeError

# الطريقة الصحيحة للوصول للـ Private عبر دالة داخلية (Method):
print(one.say_hello())  # Output: Hello Ahmed

# طريقة بايثون الخفية للوصول للخاص (Name Mangling - للتوضيح فقط):
print(one._Member__name)  # Output: Ahmed