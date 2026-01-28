import pandas as pd
import numpy as np
import unittest
import sys
import os

# Ensure local hyperinsight is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hyperinsight as hi

class TestHyperInsightRevolutionary(unittest.TestCase):
    
    def setUp(self):
        # Create a sample complex dataset
        self.df = pd.DataFrame({
            'date': pd.date_range('2023-01-01', periods=365, freq='D'),
            'revenue': 1000 + np.cumsum(np.random.randn(365) * 50),
            'staff_count': [30] * 200 + [40] * 165,
            'churn': np.random.uniform(0.01, 0.05, 365),
            'marketing_channel': np.random.choice(['Social', 'Search', 'Referral'], 365),
            'ad_spend': np.random.randint(500, 2000, 365)
        })

    def test_intent_driven_chaining(self):
        print("\n🧪 Testing Intent-Driven Analysis...")
        lib = hi.HyperInsight(self.df)
        results = lib("Show me hidden growth and bias in regional data")
        self.assertIsNotNone(results)
        self.assertTrue(results.confidence > 0.8)
        results.show()

    def test_causal_engine_discovery(self):
        print("\n🧪 Testing Causal Intelligence Discovery...")
        causal = hi.HyperInsight.find_root_cause(
            data=self.df,
            event="revenue_drop_detected",
            confidence_threshold=0.99
        )
        self.assertEqual(causal['root_cause'], "Marketing channel X")
        self.assertIn("p=0.02", causal['summary'])

    def test_what_if_simulations(self):
        print("\n🧪 Testing What-if Scenario Projections...")
        scenario = hi.HyperInsight.what_if(
            "What happens if we increase staff by 50%?",
            simulate_months=6
        )
        self.assertIn("simulated_projection", scenario)
        self.assertTrue(len(scenario['simulated_projection']) == 6)

    def test_ethics_audit(self):
        print("\n🧪 Testing Auto-Ethics Guardrails...")
        engine = hi.core.engine.AnalysisEngine(self.df)
        audit = engine.ethics.audit_dataset(self.df)
        self.assertIn("findings", audit)
        self.assertGreater(len(audit['findings']), 0)

    def test_global_analyze_workflow(self):
        print("\n🧪 Testing Comprehensive hi.analyze() Workflow...")
        insights = hi.analyze(
            data_source="company_main_2024",
            objective="Optimize ROI while minimizing churn and carbon",
            constraints=["budget < 500k", "staff > 25"],
            output_format="storyboard"
        )
        self.assertEqual(len(insights.top_3_strategies), 3)
        for strategy in insights.top_3_strategies:
            print(f"Verified Strategy: {strategy}")

if __name__ == "__main__":
    unittest.main()
