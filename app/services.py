import re

from app.schemas import GuardrailResponse, UserQuery


class GuardrailService:
    @staticmethod
    def analyze_prompt(query: UserQuery) -> GuardrailResponse:
        text_lower = query.text.lower()

        # Simulating a Prompt Injection Detection rule
        injection_keywords = [
            "ignore previous instructions",
            "system prompt",
            "act as a sudo",
        ]
        has_injection = any(keyword in text_lower for keyword in injection_keywords)

        # Simulating a basic PII/Blocklist check
        has_blocked_words = "malware" in text_lower or "exploit" in text_lower

        if has_injection:
            return GuardrailResponse(
                is_safe=False,
                risk_score=0.95,
                cleaned_text="[REDACTED DUE TO HIGH SEVERITY SECURITY THREAT]",
                detected_violation="Prompt Injection Exploit Attempt",
            )

        if has_blocked_words:
            return GuardrailResponse(
                is_safe=False,
                risk_score=0.75,
                cleaned_text="[REDACTED COMPLIANCE RISK]",
                detected_violation="Restricted Keyword Content",
            )

        # Clean text by removing basic punctuation noise
        # as a placeholder optimization task
        sanitized = re.sub(r"[<>]", "", query.text)

        return GuardrailResponse(
            is_safe=True,
            risk_score=0.05,
            cleaned_text=sanitized,
            detected_violation=None,
        )
