import datetime
import time
while True:
    print("\n╔════════════════════════════════╗")
    print("║       DIGITAL TIME TOOLS       ║")
    print("╚════════════════════════════════╝")
    print("1. 🕐 Digital Clock")
    print("2. ⏲️ Countdown Timer")
    print("3. ⏱️ Stopwatch")
    print("4. 🚪 Exit")
    choose = input("\nEnter Choice: ")
    if choose == '1':
        print("\n═══ DIGITAL CLOCK ═══")
        now = datetime.datetime.now()
        print(f"📅 {now.day:02d}-{now.month:02d}-{now.year}")
        print(f"🕐 {now.hour:02d}:{now.minute:02d}:{now.second:02d}")
    elif choose == '2':
        print("\n═══ COUNTDOWN TIMER ═══")
        seconds = int(input("Enter seconds: "))
        while seconds > 0:
            print(f"\r⏳ Time Left: {seconds} seconds", end="")
            time.sleep(1)
            seconds -= 1
        print("\n🔔 TIME'S UP! 🔔")
    elif choose == '3':
        print("\n═══ STOPWATCH ═══")
        input("Press Enter to start...")
        start = time.time()
        input("Press Enter to stop...")
        end = time.time()
        elapsed = end - start
        print(f"⏱️ Elapsed Time: {elapsed:.2f} seconds")
    elif choose == '4':
        print("\n👋 Thanks for using Digital Time Tools!")
        break
    else:
        print("❌ Invalid Choice!")
    again = input("\nUse another tool? (y/n): ").lower()
    if again != 'y':
        print("\n👋 Thanks for using Digital Time Tools!")
        break
