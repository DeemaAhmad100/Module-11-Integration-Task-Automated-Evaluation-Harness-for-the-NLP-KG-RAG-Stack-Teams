export interface Entity {
  entity_text: string;
  entity_label: string;
}

export interface ExtractResponse {
  entities: Entity[];
}

export interface KGResponse {
  cypher?: string;
  detail?: {
    reason: string;
    message: string;
  };
}

export interface RetrievedChunk {
  chunk_id: string;
}

export interface RAGResponse {
  answer: string;
  citations: string[];
  retrieved: RetrievedChunk[];
}