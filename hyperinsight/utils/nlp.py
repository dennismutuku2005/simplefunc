import re
from typing import List, Tuple, Dict, Any

class NaturalLanguageProcessor:
    """
    Symbolic NLP Processor for Intent Extraction.
    
    This component uses grammar-based parsing and semantic role labeling 
    to map high-level queries to analytical actions.
    """
    
    def __init__(self):
        self._action_verbs = ["show", "analyze", "find", "predict", "explain", "why"]
        self._target_nouns = ["growth", "opportunities", "bias", "churn", "sales", "carbon"]
        self._qualifiers = ["hidden", "top", "worst", "future", "causal"]

    def tokenize(self, text: str) -> List[str]:
        return re.findall(r'\b\w+\b', text.lower())

    def extract_triplets(self, text: str) -> List[Tuple[str, str, str]]:
        """
        Extracts Subject-Predicate-Object triplets.
        
        Example: "Show me hidden growth" -> ("Engine", "Reveal", "GrowthPatterns")
        """
        tokens = self.tokenize(text)
        triplets = []
        
        # Simple heuristic-based symbolic parser
        subject = "HyperInsight"
        predicate = "Observe"
        obj = "Data"
        
        for word in tokens:
            if word in self._action_verbs:
                predicate = word
            elif word in self._target_nouns:
                obj = word
            elif word in self._qualifiers:
                subject = word # Qualifier acts as a modifier for the scope
                
        triplets.append((subject, predicate, obj))
        return triplets

    def determine_sentiment(self, text: str) -> float:
        """Returns a numeric intensity score for the query."""
        intense_words = ["critical", "urgent", "hidden", "revolutionary", "breakthrough"]
        score = 0.5
        for word in intense_words:
            if word in text.lower():
                score += 0.1
        return min(score, 1.0)
