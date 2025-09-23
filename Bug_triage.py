
# Project 102: Bug Report Triage
# BIT Department – Sept 2025

import array   # for fixed-size arrays


# 1. INTEGERS: Generate or input values

bug_counts = [12, 25, 8, 15, 30]  # Example bug counts from different modules

total_bugs = sum(bug_counts)
average_bugs = total_bugs / len(bug_counts)
min_bugs = min(bug_counts)
max_bugs = max(bug_counts)


# 2. STRINGS: Formatted report with f-strings
report = (
    f"Bug Report Triage Summary\n"
    f"Total Bugs: {total_bugs}\n"
    f"Average Bugs per Module: {average_bugs:.2f}\n"
    f"Minimum Bugs: {min_bugs}\n"
    f"Maximum Bugs: {max_bugs}\n"
)
print(report)


# 3. BOOLEANS: Apply threshold condition

threshold = 18
if (average_bugs > threshold) and (max_bugs > 20):
    print("Status: Above Standard 🚨")
else:
    print("Status: Below Standard ✅")


# 4. LISTS: Add, remove, sort, and display

bug_list = ["UI Bug", "Crash Issue", "Performance Lag", "Security Flaw"]
print("\nOriginal Bug List:", bug_list)

# Add a new element
bug_list.append("Memory Leak")

# Remove one element based on a condition
if "Performance Lag" in bug_list:
    bug_list.remove("Performance Lag")

# Sort the list alphabetically
bug_list.sort()
print("Updated Bug List:", bug_list)


# 5. ARRAYS: Using 'array' module

bug_array = array.array("i", bug_counts)  # store integers
array_sum = sum(bug_array)
list_sum = sum(bug_counts)

print(f"\nSum from Array: {array_sum}, Sum from List: {list_sum}")


# 6. DICTIONARIES: List of records

bug_records = [
    {"id": 1, "name": "UI Bug", "value": 10},
    {"id": 2, "name": "Crash Issue", "value": 20},
    {"id": 3, "name": "Performance Lag", "value": 15},
]

# Update one record
bug_records[0]["value"] = 12

# Delete another record (remove id=2)
bug_records = [rec for rec in bug_records if rec["id"] != 2]

# Compute total of the 'value' field
total_value = sum(rec["value"] for rec in bug_records)

print("\nUpdated Bug Records:", bug_records)
print("Total Value across records:", total_value)
