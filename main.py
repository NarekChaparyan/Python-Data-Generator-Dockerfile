import pandas as pd
import numpy as np

# Generate random data
num_rows = 100
data = {
    'id': np.arange(1, num_rows + 1),
    'name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eva'], num_rows),
    'age': np.random.randint(18, 70, num_rows),
    'salary': np.round(np.random.uniform(30000, 100000, num_rows), 2)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('random_data.csv', index=False)
print("CSV file 'random_data.csv' generated successfully!")
