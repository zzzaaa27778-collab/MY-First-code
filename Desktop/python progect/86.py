# 1. تجهيز القوائم والبيانات بأطوال مختلفة
list1 = [1, 2, 3, 4, 5]                  # قائمة أرقام (5 عناصر)
list2 = ["A", "B", "C", "D"]             # قائمة حروف (4 عناصر)
tuple1 = ("Man", "Woman", "Girl", "Boy")  # تاپل شخصيات (4 عناصر)
dict1 = {"Name": "Yahya", "Age": 20, "Country": "Palestine", "Skill": "Python"} # قاموس

# 2. المرور على كل القوائم مع بعض بنفس الوقت باستخدام zip()
for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print(f"List 1 Item => {item1}")
    print(f"List 2 Item => {item2}")
    print(f"Tuple 1 Item => {item3}")
    print(f"Dict 1 Key => {item4} | Value => {dict1[item4]}")
    print("-" * 30) # خط فاصل للترتيب