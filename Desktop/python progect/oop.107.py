# ==========================================
# مرجع سريع: Class Attributes في بايثون (OOP)
# ==========================================

class Member:
    # 1. Class Attribute (متغير خاص بالكلاس كله، مشترك وثابت لكل الكائنات)
    users_num = 0  # عداد يحسب عدد المستخدمين المشتركين
    
    not_allowed_names = ["Hell", "Shit", "Baloot"] # أسماء محظورة

    def __init__(self, first_name, middle_name, last_name, gender):
        # 2. Instance Attributes (متغيرات تخص كل كائن لوحده)
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        
        # كلما تم إنشاء كائن جديد، نزيد عداد المستخدمين بواحدة
        Member.users_num += 1

    def full_name(self):
        # التحقق مما إذا كان الاسم الأول محظوراً
        if self.fname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")
        return f"{self.fname} {self.mname} {self.lname}"

    def delete_user(self):
        # عند حذف المستخدم، ننقص عداد الكلاس بواحدة
        Member.users_num -= 1
        return f"User {self.fname} Deleted."

# ------------------------------------------
# طريقة الاستخدام:
# ------------------------------------------
# الوصول لمتغير الكلاس مباشرة عبر اسم الكلاس: print(Member.users_num)
# إنشاء كائنات: m1 = Member("Osama", "Mohamed", "Elsayed", "Male")