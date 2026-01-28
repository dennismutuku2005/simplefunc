from typing import Any, Dict, List, Optional, Union
import pandas as pd
import numpy as np
from .core.engine import AnalysisEngine
from .causal.intelligence import CausalEngine
from .predictive.scenarios import ScenarioBuilder
from .ethics.bias import EthicsModule
from .narrator.storyteller import Narrator
from .utils.tensor import TensorPatternMatcher

__version__ = "1.0.0-revolutionary"
__all__ = ["HyperInsight", "analyze", "find_root_cause", "what_if", "narrate"]

class HyperInsight:
    """
    HyperInsight: The world's first Neuro-Symbolic Data Intelligence Library.
    
    This class serves as the primary entry point for intent-driven analysis.
    It combines deep learning for pattern recognition with symbolic logic 
    for verifiable reasoning.
    """
    
    def __init__(self, data: Optional[Union[pd.DataFrame, str]] = None):
        self._engine = AnalysisEngine(data)
        self._causal = CausalEngine()
        self._predictive = ScenarioBuilder()
        self._ethics = EthicsModule()
        self._narrator = Narrator()
        
    def __call__(self, query: str) -> Any:
        """Allows HyperInsight("natural language query") syntax."""
        return self._engine.process_intent(query)

    @classmethod
    def find_root_cause(cls, data: pd.DataFrame, event: str, confidence_threshold: float = 0.95):
        """Discovers causal relationships using structural equation modeling and Bayesian inference."""
        engine = CausalEngine()
        return engine.analyze_cause(data, event, confidence_threshold)

    @classmethod
    def what_if(cls, query: str, simulate_months: int = 12):
        """Simulates counterfactual scenarios using a digital twin of the temporal data."""
        builder = ScenarioBuilder()
        return builder.simulate(query, simulate_months)

    @classmethod
    def narrate(cls, data: Any, audience: str = "executive", format: str = "interactive_storyboard"):
        """Creates storytelling outputs that translate data into actionable narratives."""
        narrator = Narrator()
        return narrator.generate(data, audience, format)

def analyze(data_source: str, objective: str, constraints: List[str] = None, output_format: str = "recommendations"):
    """
    One-line revolutionary analysis entry point.
    
    Args:
        data_source: Path or identifier for the data.
        objective: Natural language description of the goal.
        constraints: Business constraints (e.g., ['budget < 1M']).
        output_format: The desired structure of the insights.
    """
    engine = AnalysisEngine(data_source)
    return engine.run_global_analysis(objective, constraints or [], output_format)
