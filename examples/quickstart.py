import sys
import os

# Add the local directory to sys.path so we can import hyperinsight
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hyperinsight as hi
import pandas as pd

def main():
    print("--- HyperInsight Revolutionary Workflow Demo ---\n")

    # One line to revolutionize everything
    insights = hi.analyze(
        data_source="all_company_data_2024",
        objective="Maximize profit while reducing carbon footprint",
        constraints=["budget<1M", "timeline<6months"],
        output_format="actionable_recommendations"
    )

    print("Top Strategies Found:")
    for strategy in insights.top_3_strategies:
        print(strategy)

    print("\n--- Additional Features ---")
    
    # Causal Intelligence
    df = pd.DataFrame({'sales': [100, 90, 80, 50], 'marketing': [10, 10, 5, 2]})
    causal = hi.HyperInsight.find_root_cause(
        data=df,
        event="sales_drop_2024"
    )
    print(f"\nRoot Cause Analysis: {causal['summary']}")

    # What-if Scenario
    scenarios = hi.HyperInsight.what_if(
        "What happens to churn if we increase support staff by 30%?",
        simulate_months=12
    )
    print(f"Scenario Projection: {scenarios['projection']}")

    # Intent-Driven
    results = hi.HyperInsight("Show me hidden growth opportunities in Q3 data")

if __name__ == "__main__":
    main()
