from datetime import datetime


class ExportService:

    @staticmethod
    def generate_markdown(

        summary=None,
        comparison=None,
        literature=None,
        notes=None,
        chat=None

    ):

        report = f"""
# AI Research Report

Generated:
{datetime.now()}

---

## Summary

{summary or "N/A"}

---

## Paper Comparison

{comparison or "N/A"}

---

## Literature Review

{literature or "N/A"}

---

## Research Notes

{notes or "N/A"}

---

## Chat History

{chat or "N/A"}

---
"""

        return report