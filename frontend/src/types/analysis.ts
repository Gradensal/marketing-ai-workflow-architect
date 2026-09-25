export type ArchitectureRecommendation =
  | "deterministic_automation"
  | "llm_assisted_workflow"
  | "agentic_workflow"
  | "keep_human_redesign_first";


export type RiskLevel =
  | "low"
  | "medium"
  | "high";


export type ExplanationStatus =
  | "available"
  | "unavailable";


export type ArchitectureAssessment = {
  recommendation: ArchitectureRecommendation;

  risk_level: RiskLevel;

  decision_strength: number;

  human_approval_required: boolean;

  human_approval_reason: string | null;

  rationale: string[];

  warnings: string[];
};


export type WorkflowExplanation = {
  why_this_approach: string;

  why_not_more_autonomy: string;

  proposed_architecture: string;

  human_checkpoint: string;

  first_experiment: string;

  success_metric: string;
};


export type WorkflowAnalysis = {
  assessment: ArchitectureAssessment;

  explanation: WorkflowExplanation | null;

  explanation_status: ExplanationStatus;

  explanation_message: string | null;
};