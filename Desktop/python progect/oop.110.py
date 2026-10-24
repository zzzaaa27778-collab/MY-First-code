# --------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# --------------------------------------------------
# الوراثة (Inheritance): هي قدرة الكلاس الفرعي (Derived/Child Class) 
# على أخذ جميع خصائص ودوال الكلاس الأساسي (Base/Parent Class) دون إعادة كتابتها.
#
# مصطلحات أساسية:
# 1. Base Class (Parent Class): الكلاس الأساسي الذي يحتوي على الخصائص العامة.
# 2. Derived Class (Child Class): الكلاس الابن الذي يرث من الأب.
# 3. Method Overriding: إعادة كتابة الدالة في الابن لتخصيص سلوك مختلف عن الأب.
# 4. super(): دالة تُستخدم لاستدعاء خصائص ودوال الـ Base Class من داخل الـ Derived Class.
# --------------------------------------------------
# 1. الـ Base Class (الكلاس الأساسي الأب)
class Food:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} Is Created From Base Class")

    def eat(self):
        print("Eat Method From Base Class")


# 2. الـ Derived Class (الكلاس الابن الذي يرث من Food)
class Apple(Food): # بين القوسين نضع اسم الكلاس الأب لكي يرث منه
    def __init__(self, name, price):
        # استخدام super() لاستدعاء الـ __init__ الخاص بالأب وإرسال الـ name له
        super().__init__(name)
        
        # إضافة خصائص جديدة خاصة بالكلاس الابن فقط
        self.price = price + 20
        print(f"{self.name} Is Created From Derived Class And Price Is {self.price}")


# --- عملية الاستدعاء والتجربة ---

# أ. إنشاء كائن من الكلاس الأب مباشرة
# food_one = Food("Pizza")

# ب. إنشاء كائن من الكلاس الابن وإرسال المتغيرات المطلوبة
food_two = Apple("Pizza", 130)

# ج. استدعاء الدالة الموروثة (eat) من الكلاس الأب عبر الكائن الابن
food_two.eat()