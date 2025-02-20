import sys

from crud import insert_expense, list_expenses, delete_expense, get_summary, get_count
from utils import parse_arguments, format_expenses_list

args = sys.argv[1:]
command, data = parse_arguments(args)

if command == 'add':
    insert_expense(float(data['amount']), data['description'], data.get('date', None))
    
elif command == 'list':
    print("# ID  Date       Description  Amount")

    expenses = format_expenses_list(list_expenses())
    for row in expenses:
        print(row)

elif command == 'summary' and data.get("month", False):
    month = int(data['month'])
    summary = get_summary(month=month)

    print(f"# Total expenses for month {month}: ${summary}")

elif command == 'summary':
    summary = get_summary()
    print(f"# Total expenses: ${summary}")

elif command == 'delete' and data.get('id', False):
    delete_expense(data["id"])
    print("# Expense deleted successfully")

