import random
import os

def clear_screen():
    # สำหรับ Linux หรือ macOS
    if os.name == 'posix':
        os.system('clear')
    # สำหรับ Windows
    elif os.name == 'nt':
        os.system('cls')

# ฟังก์ชันเลือกภาษา
def select_language():
    clear_screen()  # เคลียร์หน้าจอ
    print("Please select a language / กรุณาเลือกภาษา:")
    print("1 = English")
    print("2 = ไทย")
    
    language_choice = int(input("Enter the language number / กรอกหมายเลขภาษาที่ต้องการ: "))
    if language_choice not in [1, 2]:
        print("Invalid choice! / เลือกไม่ถูกต้อง!")
        print("=========================================================")
        return select_language()  # ให้ผู้เล่นเลือกใหม่ถ้าใส่ค่าไม่ถูกต้อง
    return language_choice

# ฟังก์ชันรับตัวเลือกของผู้เล่น
def get_user_choice(language_choice):
    if language_choice == 1:
        print("=========================================================")
        print("Choose your option:")
        print("1 = Rock")
        print("2 = Paper")
        print("3 = Scissors")
    else:
        print("=========================================================")
        print("เลือกตัวเลือกของคุณ:")
        print("1 = ค้อน")
        print("2 = กระดาษ")
        print("3 = กรรไกร")
    
    choice = int(input("Enter your choice number / กรอกหมายเลขที่ต้องการ: "))
    if choice not in [1, 2, 3]:
        if language_choice == 1:
            print("Invalid choice! Try again.")
            print("=========================================================")
        else:
            print("คุณเลือกไม่ถูกต้อง! กรุณาลองอีกครั้ง")
            print("=========================================================")
        return get_user_choice(language_choice)
    return choice

# ฟังก์ชันรับตัวเลือกของคอมพิวเตอร์
def get_computer_choice():
    return random.randint(1, 3)

# ฟังก์ชันตรวจสอบผลลัพธ์
def determine_winner(user_choice, computer_choice, language_choice):
    if language_choice == 1:
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        user_text = "You chose:"
        computer_text = "Computer chose:"
        tie_text = "It's a tie!"
        win_text = "You win!"
        lose_text = "You lose!"
    else:
        choices = {1: "ค้อน", 2: "กระดาษ", 3: "กรรไกร"}
        user_text = "คุณเลือก:"
        computer_text = "คอมพิวเตอร์เลือก:"
        tie_text = "เสมอกัน!"
        win_text = "คุณชนะ!"
        lose_text = "คุณแพ้!"
    
    print(f"\n{user_text} {choices[user_choice]}")
    print(f"{computer_text} {choices[computer_choice]}")
    
    if user_choice == computer_choice:
        return tie_text
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return win_text
    else:
        return lose_text

# ฟังก์ชันเล่นเกมหลัก
def play_game():
    language_choice = select_language()
    user_choice = get_user_choice(language_choice)
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice, language_choice)
    print(result)

# เริ่มเกม
play_game()
