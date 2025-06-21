import csv
import random
from datetime import datetime, timedelta

def generate_vibration_csv(filename, num_records=20, min_vibration=1.12, max_vibration=2.0, 
                          start_date="2025-06-01", start_time="08:00:00", interval_minutes=15):
    """
    Generate a CSV file with vibration data
    
    Parameters:
    - filename: Output CSV filename
    - num_records: Number of data records to generate
    - min_vibration: Minimum vibration value (mm/sec)
    - max_vibration: Maximum vibration value (mm/sec)
    - start_date: Starting date (YYYY-MM-DD format)
    - start_time: Starting time (HH:MM:SS format)
    - interval_minutes: Time interval between records in minutes
    """
    
    # Parse start datetime
    start_datetime = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M:%S")
    
    # Prepare data
    data = []
    for i in range(num_records):
        record_time = start_datetime + timedelta(minutes=i * interval_minutes)
        vibration = round(random.uniform(min_vibration, max_vibration), 2)
        
        data.append({
            'record': i + 1,
            'date': record_time.strftime('%Y-%m-%d'),
            'time': record_time.strftime('%H:%M:%S'),
            'vibration_mm_sec': vibration
        })
    
    # Write to CSV
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['record', 'date', 'time', 'vibration_mm_sec']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSV file '{filename}' generated successfully!")
    print(f"Records: {num_records}")
    print(f"Vibration range: {min_vibration} - {max_vibration} mm/sec")
    print(f"Time range: {start_date} {start_time} to {data[-1]['date']} {data[-1]['time']}")

def main():
    """Interactive script to generate vibration CSV files"""
    print("=== Vibration Data CSV Generator ===\n")
    
    # Get user inputs
    filename = input("Enter output filename (e.g., 'vibration_data.csv'): ").strip()
    if not filename:
        filename = "vibration_data.csv"
    
    try:
        num_records = int(input("Enter number of records (default: 20): ") or "20")
        min_vib = float(input("Enter minimum vibration value (mm/sec): "))
        max_vib = float(input("Enter maximum vibration value (mm/sec): "))
        
        if min_vib >= max_vib:
            print("Error: Minimum vibration must be less than maximum vibration")
            return
        
        start_date = input("Enter start date (YYYY-MM-DD, default: 2025-06-01): ").strip()
        if not start_date:
            start_date = "2025-06-01"
        
        start_time = input("Enter start time (HH:MM:SS, default: 08:00:00): ").strip()
        if not start_time:
            start_time = "08:00:00"
        
        interval = int(input("Enter time interval in minutes (default: 15): ") or "15")
        
        # Generate CSV
        generate_vibration_csv(
            filename=filename,
            num_records=num_records,
            min_vibration=min_vib,
            max_vibration=max_vib,
            start_date=start_date,
            start_time=start_time,
            interval_minutes=interval
        )
        
    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Uncomment the line below to run interactively
    main()
    
    # Or use directly with specific parameters:
    # generate_vibration_csv("my_vibration_data.csv", 30, 0.5, 3.2, "2025-07-01", "09:30:00", 10)