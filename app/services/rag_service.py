class RAGService:
    def __init__(self):
        self.docs = [
            "Backend development requires APIs, databases, and server-side programming.",
            "Data science requires Python, statistics, machine learning, and visualization.",
            "Consistency and daily coding improve job readiness.",
            "Projects and practice are essential for software engineering roles."
        ]

    def retrieve(self, query: str) -> str:
        query_words = set(query.lower().split())

        best_doc = ""
        max_score = 0

        for doc in self.docs:
            doc_words = set(doc.lower().split())
            score = len(query_words & doc_words)

            if score > max_score:
                max_score = score
                best_doc = doc

        return best_doc if best_doc else "No relevant knowledge found"