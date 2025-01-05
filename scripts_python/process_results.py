import csv
import sys
from prettytable import PrettyTable

if len(sys.argv) != 2:
    print("Usage: python3 process_results.py <results_file>")
    sys.exit(1)

results_file = sys.argv[1]
fields = ['label', '#samples', 'avg', 'min', 'max', 'error%', 'throughput']
summary_table = PrettyTable()
summary_table.field_names = fields

try:
    with open(results_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            summary_table.add_row([
                row['label'],
                row['#samples'],
                row['avg'],
                row['min'],
                row['max'],
                row['error%'],
                row['throughput']
            ])
    print(summary_table)
except Exception as e:
    print(f"Error processing results: {e}")
    sys.exit(1)
