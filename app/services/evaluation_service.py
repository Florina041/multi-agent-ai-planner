class EvaluationService:
    def evaluate(self, answer: str, context: str) -> float:
        if not context:
            return 0.5

        words = context.lower().split()
        match = sum(1 for w in words if w in answer.lower())

        score = match / max(len(words), 1)
        return round(score, 2)