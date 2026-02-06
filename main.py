from datetime import date
from db_config import get_connection


# ---------------- ADD RECORD ----------------
def add_record():
    workout = input("Workout name: ")
    duration = int(input("Duration (minutes): "))
    calories = int(input("Calories burned: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO fitness_records (record_date, workout, duration, calories) VALUES (%s, %s, %s, %s)",
        (date.today(), workout, duration, calories)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Record added successfully!")


# ---------------- VIEW RECORDS ----------------
def view_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM fitness_records")
    records = cursor.fetchall()

    if not records:
        print("❌ No records found.")
    else:
        print("\n--- Fitness Records ---")
        for r in records:
            print(f"ID: {r[0]} | Date: {r[1]} | Workout: {r[2]} | Duration: {r[3]} | Calories: {r[4]}")

    cursor.close()
    conn.close()


# ---------------- UPDATE RECORD ----------------
def update_record():
    record_id = int(input("Enter Record ID to update: "))

    workout = input("New workout name: ")
    duration = int(input("New duration (minutes): "))
    calories = int(input("New calories: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE fitness_records SET workout=%s, duration=%s, calories=%s WHERE id=%s",
        (workout, duration, calories, record_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Record updated successfully!")


# ---------------- DELETE RECORD ----------------
def delete_record():
    record_id = int(input("Enter Record ID to delete: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM fitness_records WHERE id=%s", (record_id,))
    conn.commit()

    cursor.close()
    conn.close()

    print("🗑️ Record deleted successfully!")


# ---------------- DAILY SUMMARY ----------------
def daily_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT SUM(duration), SUM(calories) FROM fitness_records WHERE record_date=%s",
        (date.today(),)
    )

    result = cursor.fetchone()
    duration = result[0] or 0
    calories = result[1] or 0

    print("\n--- Today's Summary ---")
    print(f"Total Duration: {duration} minutes")
    print(f"Total Calories Burned: {calories}")

    cursor.close()
    conn.close()


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n===== DAILY HEALTH & FITNESS TRACKER =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Today's Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            daily_summary()
        elif choice == "6":
            print("👋 Exiting. Stay healthy!")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
