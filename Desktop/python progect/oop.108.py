# ==========================================================
# مرجع سريع: Class Methods & Static Methods في بايثون (OOP)
# ==========================================================

class Member:
    users_num = 0  # Class Attribute مشترك

    def __init__(self, name):
        self.name = name
        Member.users_num += 1

    # 1. Class Method (دالة الكلاس)
    # - مميزاتها: تستخدم @classmethod، تأخذ cls بدلاً من self، 
    #   وتتعامل مع الكلاس ككل وليس مع كائن فردي.
    @classmethod
    def show_user_count(cls):
        return f"Total users in this class is: {cls.users_num}"

    # 2. Static Method (الدالة الثابتة / المستقلة)
    # - مميزاتها: تستخدم @staticmethod، لا تأخذ لا self ولا cls،
    #   وهي مجرد دالة مساعدة موضوعة داخل الكلاس لترتيب الكود فقط.
    @staticmethod
    def say_hello():
        return "Hello from Static Method (No self, No cls needed)!"

# --- طريقة الاستخدام المرجعية ---
# ميزة Class Method و Static Method أنه يمكن استدعاؤهما 
# مباشرة عبر اسم الكلاس بدون الحاجة لإنشاء كائن (Object):
# print(Member.show_user_count())
# print(Member.say_hello())