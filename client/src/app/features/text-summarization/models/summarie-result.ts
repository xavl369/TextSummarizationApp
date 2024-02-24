export interface SummarizeResult {
    best_sentences: string[];
    method: string;
    score_sentences: number[][];
    sentence_list: string[];
}