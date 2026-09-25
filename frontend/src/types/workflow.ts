export type WorkflowInput = {
  name: string;
  team: string;
  description: string;

  repeatability: number;
  ambiguity: number;
  tool_use: number;
  external_actions: number;
  business_risk: number;
  data_sensitivity: number;

  mandatory_human_approval: boolean;
};


export const EMPTY_WORKFLOW: WorkflowInput = {
  name: "",
  team: "",
  description: "",

  repeatability: 3,
  ambiguity: 3,
  tool_use: 3,
  external_actions: 3,
  business_risk: 3,
  data_sensitivity: 3,

  mandatory_human_approval: false,
};


export const SAMPLE_WORKFLOW: WorkflowInput = {
  name: "Campaign Message Drafting",

  team: "Product Marketing",

  description:
    "Use campaign context and audience information to create " +
    "first-draft marketing message variations that a marketer " +
    "reviews before publication.",

  repeatability: 3,
  ambiguity: 4,
  tool_use: 2,
  external_actions: 2,
  business_risk: 2,
  data_sensitivity: 2,

  mandatory_human_approval: false,
};