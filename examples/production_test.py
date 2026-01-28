import pandas as pd
import sys
import os

# Ensure local hyperinsight is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hyperinsight as hi

def production_workflow():
    print("🚀 --- HyperInsight: Real-World Production Workflow --- 🚀")
    
    # 1. REAL DATA: Loading Titanic dataset from GitHub
    dataset_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    engine = hi.core.engine.AnalysisEngine(data=dataset_url)
    
    # 2. REAL GOVERNANCE: Cleaning and Checkpointing
    print("\n--- [Governance] Manifest Purification ---")
    engine.clean_data()
    engine.state_manager.create_checkpoint("stable_prod_manifest")
    
    # 3. REAL IMPUTATION: Neutralize remaining nulls
    print("\n--- [Processing] Global Imputation ---")
    engine.fill_nulls(strategy="auto")
    
    # 4. REAL CONTEXT: Domain awareness
    engine.set_context("Industry", "Historical Transport")
    engine.set_context("Event", "Sinking of Titanic 1912")
    
    # 5. REAL INTENT: Asking standard analytical questions
    print("\n--- [Analysis] Intent Recognition ---")
    # This query triggers _analyze_trends and _detect_anomalies with real data logic
    results = engine.process_intent("Discover hidden growth and anomalies in the passenger data")
    
    print(f"\nEngine Feedback: {results}")
    for key, value in results.data.items():
        print(f"[{key.upper()}]: {value}")

    # 6. REAL OUTPUT: Final Strategy Report
    print("\n--- [Reporting] Executive Strategy Narrative ---")
    engine.write_report("production_titanic_audit.txt")
    
    print("\n✅ Production workflow finalized. Report exported to 'production_titanic_audit.txt'")

if __name__ == "__main__":
    production_workflow()
