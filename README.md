# ari-platform

Monorepo scaffold for platform and AI collaboration.

## Layout
- `services/`: Platform/infra services (gateway, ingestion, delta, storage, events, common).
- `ai/`: AI components (embeddings, retriever, rag, llm, pipelines, evaluation).
- `contracts/ai_interface.md`: Single handshake between platform and AI sides.
- `infra/`: Infrastructure provisioning.
- `docs/`: Documentation.

Extend each area with service-specific READMEs and implementation as the project evolves.
