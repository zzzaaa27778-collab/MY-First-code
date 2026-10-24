# --------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# --------------------------------------------------

# 1. Built-in Polymorphism Examples:
# دالة len تستطيع التعامل مع أنواع بيانات مختلفة (Lists, Strings, Dictionaries) وتُعطي النتيجة المناسبة لكل نوع.
print(len([1, 2, 3, 4, 5, 6]))          # Output: 6 (يعد عناصر القائمة)
print(len("Osama Elzero"))              # Output: 12 (يعد حروف النص)
print(len({"Key_One": 1, "Key_Two": 2})) # Output: 2 (يعد المفاتيح في القاموس)


# 2. Polymorphism in Classes (Method Overriding):
# تعدد الأوجه في الكلاسات يحدث عندما يرث كلاس (Child Class) من كلاس أب (Parent Class) 
# ويقوم بإعادة كتابة نفس الدالة (Method) بتفاصيل تخصه وحده.

class A:
    def do_something(self):
        # استخدام raise NotImplementedError يُعتبر كقاعدة أو عقد إجباري:
        # يعني أن أي كلاس فرعي يرث من الكلاس A يجب عليه إعادة كتابة هذه الدالة،
        # وإذا لم يفعلها سيظهر خطأ (Error) عند محاولة استدعائها.
        raise NotImplementedError("Derived Class Must Implement This Method")

class B(A):
    def do_something(self):
        print("From Class B")

class C(A):
    def do_something(self):
        print("From Class C")

# التجربة والاستدعاء:
# my_instance = A()
# my_instance.do_something()  # سيعطي خطأ لأن الأب يفرض على الأبناء تطبيق الدالة.

b_instance = B()
b_instance.do_something()  # Output: From Class B

c_instance = C()
c_instance.do_something()  # Output: From Class C
# ملف التطبيق العملي للدرس 112

class A:
    def do_something(self):
        raise NotImplementedError("Derived Class Must Implement This Method")

class B(A):
    def do_something(self):
        print("From Class B")

class C(A):
    def do_something(self):
        print("From Class C")

# جرب إنشاء كائن من B وكائن من C واستدعاء الدالة
b = B()
b.do_something()

c = C()
c.do_something()