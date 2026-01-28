import sys
import os
import pandas as pd
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import hyperinsight as hi

import io
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def test_enterprise_connectivity():
    print("🧪 [TEST 1] Testing Enterprise SQL Connectivity...")
    # Simulated SQL connection
    conn_str = "sql://admin:password@market-db.enterprise.local:5432/analytics"
    engine = hi.core.engine.AnalysisEngine(data=conn_str)
    
    print(f"✅ Ingested {len(engine.data)} rows from simulated SQL.")
    assert len(engine.data) == 1000
    assert "KPI_1" in engine.data.columns

def test_performance_monitoring():
    print("\n🧪 [TEST 2] Testing System Resource Monitoring & Audit...")
    engine = hi.core.engine.AnalysisEngine()
    
    # Trigger resource check
    engine._check_system_resources()
    audit = engine.get_performance_audit()
    
    print(f"📊 Performance Audit: {audit}")
    assert audit['reliability_score'] == 0.999
    assert "average_latency" in audit

def test_batch_processing():
    print("\n🧪 [TEST 3] Testing High-Throughput Batch Processing...")
    engine = hi.core.engine.AnalysisEngine()
    
    # Create multiple data streams
    streams = [pd.DataFrame({'x': [1,2,3]}) for _ in range(5)]
    
    print(f"⚙️ Dispatching {len(streams)} streams to batch engine...")
    batch_results = engine.batch_process(streams)
    
    print(f"✅ Batch Processing Complete. Result count: {len(batch_results)}")
    assert len(batch_results) == 5

def test_api_initialization():
    print("\n🧪 [TEST 4] Testing API Gateway Readiness...")
    from hyperinsight.api.gateway import APIInterface
    
    engine = hi.core.engine.AnalysisEngine()
    api = APIInterface(engine)
    
    # We won't block by starting the server, but we check instantiation
    print("✅ API Interface initialized and linked to Core Engine.")
    assert api.engine.trace_id is not None

def test_baseline_titanic_governance():
    print("\n🧪 [TEST 5] Testing Baseline Titanic Governance (Regression)...")
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    engine = hi.core.engine.AnalysisEngine(df)
    
    # Test cleaning + checkpoint
    engine.clean_data()
    engine.state_manager.create_checkpoint("stable")
    
    # Capture the value after cleaning but before modification
    expected_sex = engine.data['Sex'].iloc[0]
    print(f"Captured clean state 'Sex' value: {expected_sex}")

    # Test rollback
    engine.replace_values('Sex', expected_sex, 'TRANSFORMED_VALUE')
    engine.data = engine.state_manager.rollback(to="stable")
    
    print("DONE Baseline Governance tests passed.")
    assert engine.data['Sex'].iloc[0] == expected_sex

if __name__ == "__main__":
    print("START --- HYPERINSIGHT MARKET-LEVEL COMPREHENSIVE TEST SUITE ---")
    start = time.time()
    
    try:
        test_enterprise_connectivity()
        test_performance_monitoring()
        test_batch_processing()
        test_api_initialization()
        test_baseline_titanic_governance()
        
        elapsed = time.time() - start
        print(f"\nALL TESTS PASSED SUCCESSFULLY! (Total time: {elapsed:.2f}s)")
    except Exception as e:
        import traceback
        print(f"\nTEST SUITE FAILED:")
        traceback.print_exc()
        sys.exit(1)
