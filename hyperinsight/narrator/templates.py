from typing import Dict, List, Any

class NarratorTemplates:
    """
    Template repository for the Insight Narrator.
    Contains structural narrative patterns for various audiences.
    """
    
    EXECUTIVE_TEMPLATE = """
    # Executive Strategic Brief
    
    ## Objective: {objective}
    
    ### 🔑 Key Insight
    {top_insight}
    
    ### 📈 Strategic Recommendation
    1. {recommendation_1}
    2. {recommendation_2}
    
    ### 🛡️ Risk Mitigation
    Confidence Score: {confidence}%
    Ethical Audit Status: {ethics_status}
    """
    
    ANALYST_TEMPLATE = """
    # Technical Analysis Deep Dive
    
    ## Methodology
    - Engine: Neuro-Symbolic Core ({version})
    - Optimization Strategy: {optimization_mode}
    - Causal Inference: {causal_methodology}
    
    ## Observed Tensors
    {tensor_plots}
    
    ## P-Value Distribution
    Highest significance found in segment: {top_segment} (p={p_val})
    """
    
    STORYBOARD_TEMPLATE = """
    # Interactive Visual Narrative
    
    [SCENE 1: The Context]
    {context_description}
    
    [SCENE 2: The Inflection Point]
    The data reveals a non-linear shift at {inflection_point}.
    
    [SCENE 3: The Resolution]
    Proposed intervention leads to {projected_outcome}.
    """

    @classmethod
    def get_template(cls, format_type: str) -> str:
        mapping = {
            "executive": cls.EXECUTIVE_TEMPLATE,
            "technical": cls.ANALYST_TEMPLATE,
            "interactive_storyboard": cls.STORYBOARD_TEMPLATE
        }
        return mapping.get(format_type, cls.EXECUTIVE_TEMPLATE)
