# --------------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# --------------------------------------------------------------------
# - Class Called Abstract Class If It Has One or More Abstract Methods.
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @abstractmethod Decorator on The Methods.
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class.
# --------------------------------------------------------------------

# [1] الاستيراد المطلوب لتطبيق التجريد (Abstraction)
from abc import ABCMeta, abstractmethod


# [2] تعريف الكلاس الأساسي المجرد (Abstract Base Class)
# تم استخدام metaclass=ABCMeta لإعلام بايثون أن هذا الكلاس عبارة عن قالب تجريدي
class Programming(metaclass=ABCMeta):

    # الدالة الأول المجردة: تجبر أي كلاس يرث من Programming على كتابتها
    @abstractmethod
    def has_oop(self):
        pass  # نستخدم pass لأن الدالة مجردة ولا تحتوي على كود تنفيذي هنا

    # الدالة الثانية المجردة: شرط إضافي يجب تطبيقه في الكلاسات الوارثة
    @abstractmethod
    def has_name(self):
        pass


# --------------------------------------------------------------------
# [3] تطبيق الكلاسات الفرعية الوارثة (Subclasses)
# --------------------------------------------------------------------

# الكلاس الأول: Python يرث من Programming
class Python(Programming):

    # إعادة تعريف وتنفيذ الدالة المجردة الأولى (Required)
    def has_oop(self):
        return "Yes"

    # إعادة تعريف وتنفيذ الدالة المجردة الثانية (Required)
    def has_name(self):
        return "Python"


# الكلاس الثاني: Pascal يرث من Programming
class Pascal(Programming):

    # إعادة تعريف وتنفيذ الدالة المجردة الأولى (Required)
    def has_oop(self):
        return "No"

    # إعادة تعريف وتنفيذ الدالة المجردة الثانية (Required)
    def has_name(self):
        return "Pascal"


# --------------------------------------------------------------------
# [4] تجربة الكود والأخطاء المنطقية المتوقعة (Testing & Errors)
# --------------------------------------------------------------------

# تجربة صحيحة: إنشاء كائن من الكلاس الفرعي Pascal واستدعاء الدالة
one = Pascal()
print(one.has_oop())  # Output: No


# --- أخطاء شائعة يجب حظرها والتعلم منها ---

# خطأ (1): محاولة أخذ نسخة من الكلاس المجرد الرئيسي مباشرة
# test_obj = Programming()
# Naught Error: TypeError: Can't instantiate abstract class Programming with abstract methods has_name, has_oop

# خطأ (2): نسق أو نسيان تطبيق إحدى الدوال المجردة داخل الكلاس الفرعي (مثل نسيان has_name في Pascal)
# test_pascal = Pascal()
# Naught Error: TypeError: Can't instantiate abstract class Pascal with abstract method has_name