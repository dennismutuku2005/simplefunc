import pandas as pd
import sys
import os

# Add the local directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hyperinsight as hi

def main():
    print("🚀 --- HyperInsight: High-Speed Null Neutralization & Context Demo --- 🚀")
    
    # 1. Load Data with significant Nulls
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    print(f"Initial Null Count in Age: {df['Age'].isnull().sum()}")

    # 2. Initialize Engine
    engine = hi.core.engine.AnalysisEngine(df)

    # 3. SET CONTEXT WINDOW (More understanding)
    engine.set_context("Industry", "Historical Transportation")
    engine.set_context("Analysis_Goal", "Understand socio-economic survival bias")
    print(f"Engine State: {engine.get_context_summary()}")

    # 4. REVOLUTIONARY NULL FILLING (Fast & Global)
    # This fills ALL columns in one optimized call
    engine.fill_nulls(strategy="auto")
    print(f"Post-Imputation Null Count in Age: {engine.data['Age'].isnull().sum()}")
    print(f"Age sample value (now filled with mean): {engine.data['Age'].iloc[5]}")

    # 5. Intent-driven check
    results = engine.process_intent("Analyze the data after full imputation and context injection")
    results.show()

    # 6. Final report with new context
    engine.write_report("titanic_context_report.txt")
    
    print("\n✅ Process Complete. Check 'titanic_context_report.txt' for the humanized summary.")

if __name__ == "__main__":
    main()
