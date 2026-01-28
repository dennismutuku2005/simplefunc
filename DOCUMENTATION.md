# 📖 HyperInsight Comprehensive Documentation

Welcome to the definitive guide for **HyperInsight**, the market-level Neuro-Symbolic AI library for automated data intelligence.

---

## 📋 Table of Contents
1. [Installation](#-installation)
2. [Data Ingestion](#-data-ingestion)
3. [The Analysis Engine](#-the-analysis-engine)
4. [Data Governance & Rollbacks](#-data-governance)
5. [Intent-Driven Analysis](#-intent-driven-analysis)
6. [Causal Intelligence](#-causal-intelligence)
7. [Enterprise API & Scaling](#-enterprise-api)

---

## 🛠 Installation

HyperInsight requires Python 3.8+ and several enterprise-grade dependencies:

```bash
pip install pandas numpy sqlalchemy requests psutil fastapi uvicorn pydantic
```

---

## 📡 Data Ingestion
HyperInsight supports a wide variety of "Real-World" data sources.

### Loading from Files
The engine automatically detects formats:
```python
engine = hi.core.engine.AnalysisEngine(data="path/to/data.csv")
engine = hi.core.engine.AnalysisEngine(data="path/to/data.parquet")
engine = hi.core.engine.AnalysisEngine(data="path/to/spreadsheet.xlsx")
```

### Loading from URLs
```python
url = "https://example.com/data.csv"
engine = hi.core.engine.AnalysisEngine(data=url)
```

### Enterprise SQL Ingestion
```python
conn = "sql://user:pass@host:port/dbname"
engine = hi.core.engine.AnalysisEngine(data=conn)
```

---

## 🧠 The Analysis Engine
The `AnalysisEngine` is the central core. It manages the data state and triggers all analytical modules.

### Setting Context
Add domain knowledge to help the AI understand your specific industry:
```python
engine.set_context("Industry", "Retail Logistics")
engine.set_context("Region", "EMEA")
```

### Global Null Neutralization
Fix your entire dataset in one call:
```python
# Automatically applies Mean/Mode imputation based on column types
engine.fill_nulls(strategy="auto")
```

---

## 🛡 Data Governance
HyperInsight treats data as a versioned asset.

### Checkpoints
Save specific stable states of your data:
```python
engine.state_manager.create_checkpoint("after_cleaning")
```

### Rollbacks
Revert to previous states or specific checkpoints:
```python
# Revert to last change
engine.rollback()

# Revert to named milestone
engine.rollback(to="after_cleaning")
```

### The Desk View
Display the current administrative status of your workspace:
```python
engine.show_desk()
```

---

## 🔍 Intent-Driven Analysis
Stop writing `groupby` and `agg`. Use natural language queries.

### Standard Keywords
- **"Growth" / "Trends"**: Triggers statistical trend analysis.
- **"Hidden" / "Anomalies"**: Triggers 3-Sigma outlier detection.
- **"Bias" / "Ethics"**: Runs the fairness audit.

### Usage
```python
results = engine.process_intent("Analyze growth and hidden anomalies in Q4 data")
results.show()
```

---

## 🔬 Causal Intelligence
Go beyond correlation. Find the root cause of business events.

```python
impact = hi.HyperInsight.find_root_cause(
    data=df,
    event="Sales_Drop_2024",
    confidence_threshold=0.95
)
print(impact['summary'])
```

---

## 🚀 Enterprise API
Deploy HyperInsight as a microservice:

```python
from hyperinsight.api.gateway import APIInterface

api = APIInterface(engine)
# The server can be started for production use
# api.start_server(port=8080)
```

### Performance Auditing
Monitor system health:
```python
audit = engine.get_performance_audit()
print(f"Latency: {audit['average_latency']}")
```

---

*HyperInsight: Empowering organizations to ask better questions.*
