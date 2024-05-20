# Function to determine if a given year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year.\n")
    else:
        print(f"{year} is not a Leap Year!\n")
        
# Main function to handle user interaction
def main():
    while True:
        try:
            year = int(input("Enter year to check Leap year or not?: "))
            is_leap_year(year)

             # Nested while loop
            while True:
                # Ask the user if they want to check another year
                another_year =  input("Do you want to check another year (yes/no): ").strip().lower()
                if another_year == "yes":
                    break
                elif another_year == "no":
                    print("(: Thank you for using the Leap year checker :)")
                    return
                else:
                    print(f"Invalid option: '{another_year}'. Please enter 'yes' or 'no' only.")

        except ValueError:
            print("Error: Please enter numeric value!")

# Check if the script is being run directly
if __name__ == "__main__":
    main()