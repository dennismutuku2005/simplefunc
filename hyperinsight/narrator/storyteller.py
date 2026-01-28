from typing import Any, Dict, List
import json

class Narrator:
    """
    Insight Narrator Engine.
    
    Translates complex analytical outputs into human-centric 
    stories, interactive visual states, and strategic summaries.
    """
    
    def __init__(self):
        self.output_templates = {
            "executive": "strategic_summary",
            "technical": "deep_dive",
            "interactive_storyboard": "visual_flow"
        }

    def generate(self, data: Any, audience: str, format: str) -> str:
        """
        Synthesizes a narrative from the analysis data.
        """
        print(f"📖 Synthesizing {audience} narrative in {format} format...")
        
        # In a real library, this would interface with a frontend generator 
        # or export to HTML/PDF/PowerPoint.
        
        narrative_id = "hi_nar_" + str(abs(hash(str(data))))[:8]
        
        story = self._assemble_story(data, audience)
        
        print(f"✨ Narrative '{narrative_id}' generated successfully.")
        return f"https://hyperinsight-preview.local/storyboard/{narrative_id}"

    def _assemble_story(self, data: Any, audience: str) -> str:
        if audience == "executive":
            return "The bottom line is a 12% revenue increase potential through carbon-neutral routing."
        return "Regression analysis confirms non-linear elasticity in the supply chain node coefficients."

    def export_to_json(self, data: Any) -> str:
        return json.dumps({"payload": data, "metadata": {"generator": "HyperInsight Narrator"}})
