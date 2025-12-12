"""
Linear Programming Module

Brute-force Integer Linear Programming solver for product mix optimization:
- Constraint satisfaction checking
- Exhaustive feasible solution search
- Optimal solution identification
- Visualization of feasible region

Author: Victor Prefa
Course: SIG720 Machine Learning - Deakin University
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Optional


def check_constraints(A: int, B: int) -> bool:
    """
    Check if point (A, B) satisfies all problem constraints.
    
    Constraints:
        1. A + 2B <= 14 (Transportation constraint)
        2. B >= 3 (Minimum B units)
        3. A < 15 (Maximum A units)
        4. B < 15 (Maximum B units)
        5. A >= 0 (Non-negativity for A)
    
    Parameters
    ----------
    A : int
        Units of Product A
    B : int
        Units of Product B
        
    Returns
    -------
    bool
        True if all constraints satisfied, False otherwise
    """
    constraint1 = A + 2*B <= 14  # Transportation constraint
    constraint2 = B >= 3         # Minimum B units
    constraint3 = A < 15         # Maximum A units
    constraint4 = B < 15         # Maximum B units
    constraint5 = A >= 0         # Non-negativity for A
    
    return constraint1 and constraint2 and constraint3 and constraint4 and constraint5


def calculate_objective(A: int, B: int) -> int:
    """
    Calculate objective function value: Z = 3A + 4B (Revenue).
    
    Parameters
    ----------
    A : int
        Units of Product A ($3 each)
    B : int
        Units of Product B ($4 each)
        
    Returns
    -------
    int
        Total revenue
    """
    return 3 * A + 4 * B


def brute_force_solve(verbose: bool = True) -> Dict:
    """
    Solve the LP problem using brute-force enumeration of integer solutions.
    
    Problem:
        Maximize: Z = 3A + 4B
        Subject to:
            A + 2B <= 14
            B >= 3
            A < 15, B < 15
            A >= 0
    
    Parameters
    ----------
    verbose : bool
        Whether to print detailed output
        
    Returns
    -------
    dict
        Solution containing optimal point, value, and all feasible points
    """
    # Search ranges based on constraints
    A_range = range(0, 15)    # A values (A < 15, A >= 0)
    B_range = range(3, 15)    # B values (B >= 3, B < 15)
    
    # Initialize tracking variables
    max_val = float('-inf')
    max_sol = (0, 0)
    feasible_points = []
    
    if verbose:
        print("Linear Programming Optimization")
        print("=" * 50)
        print("Problem: Maximize Z = 3A + 4B")
        print("Constraints: A + 2B ≤ 14, B ≥ 3, A < 15, B < 15, A ≥ 0")
        print("\nSearching for optimal solution...")
        print("-" * 50)
        print(f"{'Point (A, B)':<15} {'Feasible':<12} {'Revenue ($)':<12}")
        print("-" * 50)
    
    # Enumerate all integer combinations
    for A in A_range:
        for B in B_range:
            if check_constraints(A, B):
                obj_val = calculate_objective(A, B)
                feasible_points.append((A, B, obj_val))
                
                if verbose:
                    print(f"({A:2d}, {B:2d}){'':<8} {'✓':<12} ${obj_val:<11}")
                
                # Update maximum if better solution found
                if obj_val > max_val:
                    max_val = obj_val
                    max_sol = (A, B)
    
    if verbose:
        print("-" * 50)
        print(f"\n{'='*50}")
        print("OPTIMAL SOLUTION FOUND")
        print(f"{'='*50}")
        print(f"Product A units: {max_sol[0]}")
        print(f"Product B units: {max_sol[1]}")
        print(f"Maximum Revenue: ${max_val}")
        print(f"Feasible Solutions: {len(feasible_points)}")
    
    return {
        'optimal_A': max_sol[0],
        'optimal_B': max_sol[1],
        'max_revenue': max_val,
        'feasible_points': feasible_points,
        'num_feasible': len(feasible_points)
    }


def verify_constraints(A: int, B: int, verbose: bool = True) -> Dict:
    """
    Verify and display constraint satisfaction for a solution.
    
    Parameters
    ----------
    A : int
        Units of Product A
    B : int
        Units of Product B
    verbose : bool
        Whether to print results
        
    Returns
    -------
    dict
        Constraint satisfaction details
    """
    constraints = {
        'transportation': {
            'expression': f'{A} + 2({B}) = {A + 2*B}',
            'constraint': 'A + 2B ≤ 14',
            'satisfied': A + 2*B <= 14,
            'binding': A + 2*B == 14
        },
        'min_B': {
            'expression': f'{B} ≥ 3',
            'constraint': 'B ≥ 3',
            'satisfied': B >= 3,
            'binding': B == 3
        },
        'max_A': {
            'expression': f'{A} < 15',
            'constraint': 'A < 15',
            'satisfied': A < 15,
            'binding': False
        },
        'max_B': {
            'expression': f'{B} < 15',
            'constraint': 'B < 15',
            'satisfied': B < 15,
            'binding': False
        },
        'non_negativity': {
            'expression': f'{A} ≥ 0',
            'constraint': 'A ≥ 0',
            'satisfied': A >= 0,
            'binding': A == 0
        }
    }
    
    if verbose:
        print(f"\nConstraint Verification for ({A}, {B}):")
        print("-" * 45)
        for name, details in constraints.items():
            status = '✓' if details['satisfied'] else '✗'
            binding = ' (BINDING)' if details['binding'] else ''
            print(f"{details['constraint']}: {details['expression']} {status}{binding}")
    
    return constraints


def plot_feasible_region(solution: Dict, save_path: Optional[str] = None):
    """
    Plot the feasible region and optimal solution.
    
    Parameters
    ----------
    solution : dict
        Solution from brute_force_solve()
    save_path : str, optional
        Path to save the figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create plotting range
    A_plot = np.linspace(0, 16, 100)
    
    # Plot constraints
    # Constraint 1: A + 2B <= 14 => B <= (14 - A)/2
    B1 = (14 - A_plot) / 2
    ax.plot(A_plot, B1, 'r-', label='A + 2B ≤ 14', linewidth=2)
    
    # Constraint 2: B >= 3
    ax.axhline(y=3, color='blue', linestyle='-', label='B ≥ 3', linewidth=2)
    
    # Constraint 3: A < 15
    ax.axvline(x=15, color='green', linestyle='--', label='A < 15', linewidth=2)
    
    # Constraint 4: B < 15
    ax.axhline(y=15, color='orange', linestyle='--', label='B < 15', linewidth=2)
    
    # Fill feasible region
    feasible_A = [p[0] for p in solution['feasible_points']]
    feasible_B = [p[1] for p in solution['feasible_points']]
    ax.scatter(feasible_A, feasible_B, c='purple', s=50, alpha=0.6, 
               label=f'Feasible Points ({solution["num_feasible"]})')
    
    # Plot optimal point
    ax.scatter(solution['optimal_A'], solution['optimal_B'], 
               c='red', s=200, marker='*', zorder=5,
               label=f'Optimal: ({solution["optimal_A"]}, {solution["optimal_B"]})')
    
    # Add iso-profit lines
    for z in [20, 30, 36]:
        B_iso = (z - 3*A_plot) / 4
        ax.plot(A_plot, B_iso, '--', alpha=0.3, label=f'Z = {z}' if z == 36 else '')
    
    ax.set_xlabel('Product A (units)', fontsize=12)
    ax.set_ylabel('Product B (units)', fontsize=12)
    ax.set_title('Linear Programming: Feasible Region and Optimal Solution\n'
                f'Max Revenue: ${solution["max_revenue"]}', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 16)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Figure saved to: {save_path}")
    
    plt.show()


def sensitivity_analysis(solution: Dict) -> Dict:
    """
    Perform basic sensitivity analysis on the optimal solution.
    
    Parameters
    ----------
    solution : dict
        Solution from brute_force_solve()
        
    Returns
    -------
    dict
        Sensitivity analysis results
    """
    A_opt = solution['optimal_A']
    B_opt = solution['optimal_B']
    
    print("\nSensitivity Analysis")
    print("=" * 50)
    
    # Slack analysis
    transport_slack = 14 - (A_opt + 2*B_opt)
    min_B_slack = B_opt - 3
    
    print(f"\nSlack Variables:")
    print(f"  Transportation (A + 2B ≤ 14): {transport_slack} units slack")
    print(f"  Minimum B (B ≥ 3): {min_B_slack} units slack")
    
    # What-if: increase transportation capacity
    print(f"\nWhat-if: Transportation capacity increases to 16?")
    new_max = 0
    new_sol = (0, 0)
    for A in range(0, 15):
        for B in range(3, 15):
            if A + 2*B <= 16 and A >= 0:  # Modified constraint
                obj = 3*A + 4*B
                if obj > new_max:
                    new_max = obj
                    new_sol = (A, B)
    
    print(f"  New optimal: ({new_sol[0]}, {new_sol[1]}) with revenue ${new_max}")
    print(f"  Revenue increase: ${new_max - solution['max_revenue']}")
    
    return {
        'transport_slack': transport_slack,
        'min_B_slack': min_B_slack,
        'shadow_price_estimate': (new_max - solution['max_revenue']) / 2
    }


def demo():
    """Demonstrate LP solving."""
    print("Linear Programming Optimization Demo")
    print("=" * 50)
    
    # Solve the problem
    solution = brute_force_solve(verbose=True)
    
    # Verify constraints
    verify_constraints(solution['optimal_A'], solution['optimal_B'])
    
    # Sensitivity analysis
    sensitivity_analysis(solution)
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Optimal Bundle: {solution['optimal_A']} units A + {solution['optimal_B']} units B")
    print(f"Maximum Revenue: ${solution['max_revenue']}")
    print("Business Insight: Prioritize Product A despite lower unit price")
    print("                  due to transportation constraint coefficients.")


if __name__ == "__main__":
    demo()
