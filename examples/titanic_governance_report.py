import pandas as pd
import sys
import os

# Add the local directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hyperinsight as hi

def main():
    print("🚢 --- HyperInsight: Titanic Advanced Governance & Analysis --- 🚢")
    
    # 1. Loading the original dataset
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    print(f"📥 Fetching raw historical manifest from: {url}")
    try:
        df = pd.read_csv(url)
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return

    # Initialize the revolutionary engine
    engine = hi.core.engine.AnalysisEngine(df)
    engine.show_desk()

    # 2. Data Cleaning with Versioning
    print("\n[ACTION] Commencing autonomous data purification...")
    # Titanic data usually has missing values in 'Age' and 'Cabin'
    engine.clean_data()
    engine.state_manager.create_checkpoint("purified_manifest")

    # 3. Targeted Data Transformation
    print("\n[ACTION] Normalizing categorical indicators...")
    # Replace 'male' and 'female' for better numeric processing if needed, or just demo the tool
    engine.replace_values('Sex', 'male', 'M')
    engine.replace_values('Sex', 'female', 'F')
    
    # 4. Intent-Driven Analysis on the modified state
    print("\n[ANALYSIS] Processing survival patterns after normalization...")
    results = engine.process_intent("What are the hidden survival patterns for gender M and F across passenger classes?")
    results.show()

    # 5. Rollback Demonstration
    print("\n[GOVERNANCE] Testing state restoration...")
    print("Let's assume our Gender normalization ('M'/'F') wasn't compatible with our downstream models.")
    print(f"Current 'Sex' samples: {engine.data['Sex'].iloc[0]}")
    
    engine.rollback(to="purified_manifest")
    print(f"Restored 'Sex' samples: {engine.data['Sex'].iloc[0]}")

    # 6. Safety Lock
    print("\n[POLICY] Locking data state for archival...")
    engine.state_manager.set_lock(True)

    # 7. Final Humanized Reporting
    print("\n[REPORTING] Synthesizing narrative for shipping authorities...")
    report_file = "titanic_safety_report.txt"
    engine.write_report(report_file)
    
    print(f"\n✅ Analysis complete. Strategic findings exported to: {report_file}")
    
    print("\n--- Preview of Generated Strategic Report ---")
    with open(report_file, "r") as f:
        print(f.read())

if __name__ == "__main__":
    main()
