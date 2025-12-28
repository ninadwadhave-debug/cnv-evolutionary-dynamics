import numpy as np
import matplotlib.pyplot as plt

def run_simulation(pop_size, selection_coeff, generations, initial_freq):
    """
    Simulates the frequency of a gene duplication (CNV) over time.
    
    Args:
        pop_size (int): Number of individuals (N)
        selection_coeff (float): Advantage of duplication (s). 0 = neutral.
        generations (int): Max time to run.
        initial_freq (float): Starting frequency (usually 1/2N).
    
    Returns:
        list: A history of allele frequencies over time.
    """
    # 1. Initialize
    frequency = initial_freq
    history = [frequency]
    
    # 2. Run the Generation Loop
    for _ in range(generations):
        if frequency == 0 or frequency == 1: 
            break # Stop if lost (0) or fixed (1)
        
        # Calculate Fitness (Selection)
        # If selection_coeff > 0, the duplication provides an advantage
        fitness = 1 + selection_coeff
        avg_fitness = (frequency * fitness) + ((1 - frequency) * 1)
        prob_selection = (frequency * fitness) / avg_fitness
        
        # Random Sampling (Drift)
        # We use a Binomial distribution to simulate random mating
        # 2 * pop_size because plants are diploid (2 alleles per individual)
        successes = np.random.binomial(2 * pop_size, prob_selection)
        frequency = successes / (2 * pop_size)
        
        history.append(frequency)
        
    return history

# --- TEST BLOCK ---
# This runs only if you execute this file directly to test it
if __name__ == "__main__":
    print("Starting simulation test...")
    
    # Parameters based on Arabidopsis population genetics
    N = 100       # Small population size for testing
    s = 0.05      # 5% fitness advantage
    gens = 200    # Max generations
    
    trajectory = run_simulation(N, s, gens, 1/(2*N))
    
    print(f"Simulation finished in {len(trajectory)} generations.")
    print(f"Final Frequency: {trajectory[-1]}")

    # Plotting & Saving
    plt.plot(trajectory)
    plt.title(f"CNV Trajectory (N={N}, s={s})")
    plt.xlabel("Generations")
    plt.ylabel("Frequency")
    
    # SAVE the image instead of showing it
    output_filename = "test_simulation.png"
    plt.savefig(output_filename)
    print(f"SUCCESS: Graph saved as {output_filename}")