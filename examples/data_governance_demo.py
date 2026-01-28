import pandas as pd
import sys
import os

# Add the local directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hyperinsight as hi

def main():
    print("🚀 --- HyperInsight Data Governance & AI Insights Demo --- 🚀")
    
    # 1. Setup sample messy data
    df = pd.DataFrame({
        'A': [1, 2, None, 4, 1], # Has NaN and Duplicate
        'B': ['low', 'high', 'high', 'med', 'low']
    })
    
    # Initialize Engine
    engine = hi.core.engine.AnalysisEngine(df)
    
    # 2. Show Desk Initial Status
    engine.show_desk()
    
    # 3. Clean Data
    print("\n--- Cleaning Data ---")
    engine.clean_data()
    
    # 4. Create Checkpoint
    engine.state_manager.create_checkpoint("post_clean")
    
    # 5. Replace Values
    print("\n--- Replacing Values ---")
    engine.replace_values('B', 'med', 'medium')
    
    # 6. Show Desk again
    engine.show_desk()
    
    # 7. Rollback to Checkpoint
    print("\n--- Testing Rollback ---")
    print("Rolling back to 'post_clean' (should undo the 'med' -> 'medium' change)...")
    engine.rollback(to="post_clean")
    print(f"Current B column values (after rollback):\n{engine.data['B'].values}")
    
    # 8. Test Rollback Lock
    print("\n--- Testing Administrative Lock ---")
    engine.state_manager.set_lock(locked=True)
    try:
        engine.rollback()
    except PermissionError as e:
        print(f"⛔ Caught Expected Error: {e}")
    
    # 9. Human-like Output to TXT
    print("\n--- Generating Humanized AI Report ---")
    report_msg = engine.write_report("final_insights.txt")
    print(report_msg)
    
    print("\n--- Verifying TXT Content ---")
    with open("final_insights.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    main()
