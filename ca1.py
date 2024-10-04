import datetime

records = []

def add_record():
    year = int(input("Enter Year: "))
    country = input("Enter Country Name: ")
    player = input("Enter Player Name: ")
    win_or_loss = input("Enter Win or Loss: ")    
    event = input("Enter Event Name: ")
    sport = input("Enter Sport: ")
    

    record = {
        'year': year,
        'country': country,
        'player': player,
        'win_or_loss': win_or_loss,        
        'event': event,
        'sport': sport
        
    }
    records.append(record)
    print("Record added successfully!")

def delete_record():
    if not records:
        print("No records to delete.")
        return
    
    print("Select the record to delete:")
    for idx, record in enumerate(records, start=1):
        print(f"{idx}. {record['player']} ({record['event']} - {record['year']})")

    choice = int(input("Enter the record number to delete: "))
    
    if 1 <= choice <= len(records):
        del records[choice - 1]
        print("Record deleted successfully!")
    else:
        print("Invalid selection!")

def view_all_records():
    if not records:
        print("No records available.")
        return

    for record in records:
        if(record['country']=="Trinidad and Tobago"):
            print(f"In {record['year']}, the player {record['player']} won a {record['medal']} in the event of {record['event']} ({record['sport']}) for {record['country']}.")
        

def view_last_5_years_winners():
    if not records:
        print("No records available.")
        return
   
    
    current_year = datetime.datetime.now().year
    filtered_records = [r for r in records if  r['win_or_loss'].lower() == 'win' and r['year'] >= current_year - 5 and record['country']!="Trinidad and Tobago"]

    if not filtered_records:
        print(f"No winners found  in the last 5 years.")
    else:
        print(f"Last 5 years' winners for :")
        
        for record in filtered_records:
            print(f"In {record['year']}, the player {record['player']} won a {record['medal']} in the event of {record['event']} ({record['sport']}) for {record['country']}.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add a New Record")
        print("2. Delete a Record")
        print("3. View All Records")
        print("4. View Last 5 Years' Winners in a Sport")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            delete_record()
        elif choice == '3':
            view_all_records()
        elif choice == '4':
            view_last_5_years_winners()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()