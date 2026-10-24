# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
#
# Magic Methods (Dunder Methods):
# هي دوال تبدأ وتنتهي بـ __ تستدعيها بايثون تلقائياً في حالات معينة.
#
# __init__    : Called Automatically When Instantiating Class
#               (تُستدعى تلقائياً عند إنشاء كائن جديد من الكلاس)
#
# self.__class__ : The class to which a class instance belongs
#               (خاصية ترجع الكلاس الذي ينتمي إليه الكائن)
#
# __str__     : Gives a Human-Readable Output of the Object
#               (تُرجع نصاً مفهوم للرؤية عند طباعة الكائن بـ print)
#
# __len__     : Returns the Length of the Container
#               Called When We Use the Built-in len() Function on the Object
#               (تُستدعى عندما نستخدم دالة len() على الكائن وتحدد ماذا ترجع)
# --------------------------------------------------

# الهيكل الأساسي للأكواد كما كتبها في الفيديو:

class Skill:
    def __init__(self):
        # مصفوفة أو قائمة تحتوي البيانات الأساسية
        self.skills = ["Html", "Css", "Js"]

    def __str__(self):
        # تحديد الشكل النصي عند الاستدعاء
        return f"This is My Skills => {self.skills}"

    def __len__(self):
        # تحديد القيمة العددية التي ترجعها دالة len
        return len(self.skills)

# ملاحظة إضافية للبحث والتطوير بالمستقبل:
# dir(str) أو dir(int) ترجع لك جميع الـ Magic Methods المتاحة للأنواع المختلفة