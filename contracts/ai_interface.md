# 🧾 AI Interface Contract — ARI Platform

## Purpose
This document defines the strict boundary between the Platform Layer and the AI / Intelligence Layer.
Neither side makes assumptions about the other beyond what is specified here.

## 1️⃣ Responsibilities

### 🧱 Platform Layer (Vijay)
The platform guarantees:

- Clean, normalized documents
- Deterministic IDs & versioning
- Idempotent ingestion & updates
- Reliable event delivery
- Stable APIs for data access
- Persistence of AI outputs

### 🧠 AI Layer (Renu)
The AI layer is responsible for:

- Embeddings generation
- Vector indexing & retrieval
- RAG pipelines
- LLM reasoning & enrichment
- Evaluation & improvement loops

## 2️⃣ Data Guarantees From Platform → AI

### Document Object
```json
{
  "document_id": "string",
  "version": 3,
  "source": "ingestion",
  "title": "string",
  "content": "string",
  "metadata": {
    "created_at": "ISO-8601",
    "updated_at": "ISO-8601",
    "tags": ["string"],
    "language": "en"
  }
}
```

**Guarantees:**

- `document_id` + `version` is immutable
- Content never mutates for a given version
- New content always increments version

## 3️⃣ Events Exposed by Platform

| Event | Description |
|-------|-------------|
| `CONTENT_CHANGED` | A new document version is ready |
| `DATA_READY_FOR_AI` | Document is safe for AI processing |
| `DOCUMENT_DELETED` | Historical cleanup event |

**Example:**

```json
{
  "event_type": "DATA_READY_FOR_AI",
  "payload": {
    "document_id": "doc-123",
    "version": 3
  }
}
```

## 4️⃣ APIs Exposed by Platform

### 🔎 Fetch Document
```
GET /api/documents/{document_id}/{version}
```

Returns full Document Object.

### 🧾 Store AI Output
```
POST /api/ai/enrichment
```

```json
{
  "document_id": "doc-123",
  "version": 3,
  "model": "gpt-4.2",
  "summary": "string",
  "entities": ["string"],
  "confidence": 0.94,
  "artifacts": {}
}
```

## 5️⃣ Outputs From AI → Platform

The AI layer must return:

- Enriched content
- Model metadata
- Confidence scores
- Evaluation metrics (optional)

The platform persists all AI outputs and exposes them via API.

## 6️⃣ Failure & Retry Semantics

- AI processing is **at‑least‑once**
- Platform ingestion is **exactly‑once**
- AI must treat all inputs as idempotent
- All AI outputs must be safely repeatable

## 7️⃣ Versioning & Compatibility

- Platform schema changes are backward compatible
- AI model versions are explicit
- Breaking changes require new contract version

## 8️⃣ Design Rule

**No direct DB access between layers.**
**No cross‑service imports.**
**All communication happens via this contract.**
