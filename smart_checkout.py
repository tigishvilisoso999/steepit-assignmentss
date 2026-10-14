# smart_checkout.py

# მომხმარებლის მონაცემების შეყვანა
cart_total = float(input("შეიყვანეთ კალათის ღირებულება: "))
user_status = input("შეიყვანეთ მომხმარებლის სტატუსი (regular, vip, admin): ").lower()
has_promo_code = input("გაქვთ პრომოკოდი? (კი/არა): ").lower() == "კი"
loyalty_points = int(input("შეიყვანეთ დაგროვებული ქულები: "))
delivery_city = input("შეიყვანეთ ქალაქი: ").lower()
is_account_active = input("აქტიურია ანგარიში? (კი/არა): ").lower() == "კი"

# 1. ანგარიშის შემოწმება (Guard Clause)
if not is_account_active:
    print("ანგარიში არააქტიურია. შეკვეთა ვერ განხორციელდება.")

elif cart_total <= 0:
    print("კალათა ცარიელია. დაამატეთ პროდუქტები.")

elif cart_total < 8:
    print("შეკვეთის მინიმალური ღირებულება არის 8 ლარი.")

else:
    # 2. ფასდაკლების გამოთვლა
    discount = 0

    if user_status == "vip":
        discount = 20

        if loyalty_points >= 500:
            discount = 25

    elif user_status == "regular":
        if has_promo_code or cart_total >= 150:discount = 10

    elif user_status == "admin":
        discount = 50

    # ფასდაკლებული თანხა
    discount_amount = cart_total * discount / 100
    final_total = cart_total - discount_amount

    # 3. მიტანის საფასურის გამოთვლა
    if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
        if final_total > 100:
            delivery_fee = 0
        else:
            delivery_fee = 5
    else:
        delivery_fee = 15
        print("თქვენს ქალაქში მიტანის საფასური 15 ლარია.")

    # 4. საბოლოო შედეგი
    final_total += delivery_feeprint("\n--- შეკვეთის დეტალები ---")
    print(f"კალათის ღირებულება: {cart_total:.2f} ლარი")
    print(f"ფასდაკლება: {discount}%")
    print(f"დაზოგილი თანხა: {discount_amount:.2f} ლარი")
    print(f"მიტანის საფასური: {delivery_fee:.2f} ლარი")
    print(f"საბოლოო გადასახდელი თანხა: {final_total:.2f} ლარი")
