import numpy as np
import matplotlib.pyplot as plt
from simulation import run_simulation 

# Settings
trials = 500
N = 100 
generations = 1000

# 1. Run Neutral Scenario (Drift Only)
print("Running Neutral Scenario (s=0)...")
neutral_counts = 0
for _ in range(trials):
    traj = run_simulation(N, 0, generations, 1/(2*N))
    if traj[-1] == 1.0: # Did it reach fixation?
        neutral_counts += 1

# 2. Run Selection Scenario (Adaptive Evolution)
print("Running Selection Scenario (s=0.05)...")
select_counts = 0
for _ in range(trials):
    # s=0.05 represents a strong adaptive driver
    traj = run_simulation(N, 0.05, generations, 1/(2*N))
    if traj[-1] == 1.0:
        select_counts += 1

# 3. Calculate Results
prob_neutral = neutral_counts / trials
prob_select = select_counts / trials

print(f"Fixation Probability (Neutral): {prob_neutral:.3f}")
print(f"Fixation Probability (Selection): {prob_select:.3f}")

# 4. Save the Bar Chart
labels = ['Neutral', 'Positive Selection']
values = [prob_neutral, prob_select]

plt.figure() # Create a new figure
plt.bar(labels, values, color=['gray', 'green'])
plt.ylabel("Probability of Fixation")
plt.title("Impact of Selection on CNV Maintenance")

output_filename = "results_chart.png"
plt.savefig(output_filename)
print(f"SUCCESS: Experiment graph saved as {output_filename}")